import socket


class Flasher:
    def __init__(self):

        self.socket_flasher = None
        self.address = '129.194.52.90'
        self.host = 50001
        self.buffer_size = 32
        self.code_prod = 0xA5
        self.cr = 0x0D
        self.lf = 0x0A

        self.cmd_status = [0xE0, self.code_prod, self.cr, self.lf]
        self.cmd_stop = [0xF0, self.code_prod, self.cr, self.lf]
        self.cmd_start = [0xFC, self.code_prod, self.cr, self.lf]
        self.cmd_reset = [0xF3, self.code_prod, self.cr, self.lf]

        self.bin_pulse_started = 0
        self.mask = 0b11111

        '''
        data frame structure:
        =====================
        The dictonary decleared below for request and answer follow the data frame structure
        '''

        self.data_frame_req = {'led_status': {}, 'led_voltage': {}, 'pulse_duration': {}, 'pulse_frequency': {},
                               'freq_divider': {}, 'pulse_width': {}, 'io_status': {}, 'code_product': {},
                               'cr': {}, 'lf': {}}

        self.data_frame_req['led_status']['word_msb'] = 0b001 << 5
        self.data_frame_req['led_status']['led_order'] = [13, 8, 5, 3, 7, 2, 1, 4, 6, 11, 9, 12, 10]
        self.data_frame_req['led_status']['offset'] = list(range(5)) + list(range(5)) + list(range(3))
        self.data_frame_req['led_status']['frame_num'] = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2]
        self.data_frame_req['led_status']['bytes'] = [0b001 << 5] * 3

        self.data_frame_req['led_voltage']['word_msb'] = 0b010 << 5
        self.data_frame_req['led_voltage']['offset_msb'] = 5
        self.data_frame_req['led_voltage']['offset_lsb'] = 0
        self.data_frame_req['led_voltage']['bytes'] = [0b010 << 5] * 2

        self.data_frame_req['pulse_duration']['word_msb'] = 0b011 << 5
        self.data_frame_req['pulse_duration']['offset_msb'] = 5
        self.data_frame_req['pulse_duration']['offset_lsb'] = 0
        self.data_frame_req['pulse_duration']['bytes'] = [0b011 << 5] * 2

        self.data_frame_req['pulse_frequency']['word_msb'] = 0b011 << 5
        self.data_frame_req['pulse_frequency']['offset_msb'] = 15
        self.data_frame_req['pulse_frequency']['offset_cmsb'] = 10
        self.data_frame_req['pulse_frequency']['offset_clsb'] = 5
        self.data_frame_req['pulse_frequency']['offset_lsb'] = 0
        self.data_frame_req['pulse_frequency']['bytes'] = [0b011 << 5] * 4

        self.data_frame_req['freq_divider']['word_msb'] = 0b011 << 5
        self.data_frame_req['freq_divider']['offset_msb'] = 10
        self.data_frame_req['freq_divider']['offset_csb'] = 5
        self.data_frame_req['freq_divider']['offset_lsb'] = 0
        self.data_frame_req['freq_divider']['bytes'] = [0b011 << 5] * 3

        self.data_frame_req['pulse_width']['word_msb'] = 0b011 << 5
        self.data_frame_req['pulse_width']['offset_msb'] = 5
        self.data_frame_req['pulse_width']['offset_lsb'] = 0
        self.data_frame_req['pulse_width']['bytes'] = [0b011 << 5] * 2

        self.data_frame_req['io_status']['word_msb'] = 0b101 << 5
        self.data_frame_req['io_status']['offset_light_pulse'] = 0
        self.data_frame_req['io_status']['offset_trigger_out'] = 1
        self.data_frame_req['io_status']['offset_fiber_1'] = 2
        self.data_frame_req['io_status']['offset_fiber_2'] = 3
        self.data_frame_req['io_status']['bytes'] = [0b101 << 5]

        self.data_frame_req['code_product']['bytes'] = [self.code_prod]
        self.data_frame_req['cr']['bytes'] = [self.cr]
        self.data_frame_req['lf']['bytes'] = [self.lf]

        '''
        Structure of answer expected for all commands except for the reset
        '''

        self.data_frame_ans = {'led_status': {}, 'led_voltage': {}, 'pulse_duration': {}, 'pulse_frequency': {},
                               'freq_divider': {}, 'pulse_width': {}, 'temperature': {}, 'voltage_status': {},
                               'io_status': {}, 'code_product': {}, 'product_number': {}, 'cr': {}, 'lf': {}}

        self.data_frame_ans['led_status']['word_msb'] = 0b001 << 5
        self.data_frame_ans['led_status']['item_num'] = 13
        self.data_frame_ans['led_status']['led_order'] = [13, 8, 5, 3, 7, 2, 1, 4, 6, 11, 9, 12, 10]

        self.data_frame_ans['led_status']['item_list'] = ['led_13', 'led_8', 'led_5', 'led_3', 'led_7', 'led_2',
                                                          'led_1', 'led_4', 'led_6', 'led_11', 'led_9', 'led_12',
                                                          'led_10']
        self.data_frame_ans['led_status']['offset'] = list(range(5)) + list(range(5)) + list(range(3))
        self.data_frame_ans['led_status']['word_num'] = 3
        self.data_frame_ans['led_status']['bytes'] = []
        self.data_frame_ans['led_status']['value'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.data_frame_ans['led_voltage']['word_msb'] = 0b010 << 5
        self.data_frame_ans['led_voltage']['word_id'] = ['msb', 'lsb']
        self.data_frame_ans['led_voltage']['offset_msb'] = 5
        self.data_frame_ans['led_voltage']['offset_lsb'] = 0
        self.data_frame_ans['led_voltage']['word_num'] = 2
        self.data_frame_ans['led_voltage']['bytes'] = []
        self.data_frame_ans['led_voltage']['value'] = 0
        self.data_frame_ans['led_voltage']['convert'] = self.convert_volt_ans_to_num

        self.data_frame_ans['pulse_duration']['word_msb'] = 0b011 << 5
        self.data_frame_ans['pulse_duration']['word_id'] = ['msb', 'lsb']
        self.data_frame_ans['pulse_duration']['offset_msb'] = 5
        self.data_frame_ans['pulse_duration']['offset_lsb'] = 0
        self.data_frame_ans['pulse_duration']['word_num'] = 2
        self.data_frame_ans['pulse_duration']['bytes'] = []
        self.data_frame_ans['pulse_duration']['value'] = 0

        self.data_frame_ans['pulse_frequency']['word_msb'] = 0b011 << 5
        self.data_frame_ans['pulse_frequency']['word_id'] = ['msb', 'cmsb', 'clsb', 'lsb']
        self.data_frame_ans['pulse_frequency']['offset_msb'] = 15
        self.data_frame_ans['pulse_frequency']['offset_cmsb'] = 10
        self.data_frame_ans['pulse_frequency']['offset_clsb'] = 5
        self.data_frame_ans['pulse_frequency']['offset_lsb'] = 0
        self.data_frame_ans['pulse_frequency']['word_num'] = 4
        self.data_frame_ans['pulse_frequency']['bytes'] = []
        self.data_frame_ans['pulse_frequency']['value'] = 0
        self.data_frame_ans['pulse_frequency']['convert'] = self.convert_freq_ans_to_num

        self.data_frame_ans['freq_divider']['word_msb'] = 0b011 << 5
        self.data_frame_ans['freq_divider']['word_id'] = ['msb', 'csb', 'lsb']
        self.data_frame_ans['freq_divider']['offset_msb'] = 10
        self.data_frame_ans['freq_divider']['offset_csb'] = 5
        self.data_frame_ans['freq_divider']['offset_lsb'] = 0
        self.data_frame_ans['freq_divider']['word_num'] = 3
        self.data_frame_ans['freq_divider']['bytes'] = []
        self.data_frame_ans['freq_divider']['value'] = 0

        self.data_frame_ans['pulse_width']['word_msb'] = 0b011 << 5
        self.data_frame_ans['pulse_width']['word_id'] = ['msb', 'lsb']
        self.data_frame_ans['pulse_width']['offset_msb'] = 5
        self.data_frame_ans['pulse_width']['offset_lsb'] = 0
        self.data_frame_ans['pulse_width']['word_num'] = 2
        self.data_frame_ans['pulse_width']['bytes'] = []
        self.data_frame_ans['pulse_width']['value'] = 0

        self.data_frame_ans['temperature']['word_msb'] = 0b100 << 5
        self.data_frame_ans['temperature']['word_id'] = ['msb', 'csb', 'lsb']
        self.data_frame_ans['temperature']['offset_msb'] = 10
        self.data_frame_ans['temperature']['offset_csb'] = 5
        self.data_frame_ans['temperature']['offset_lsb'] = 0
        self.data_frame_ans['temperature']['word_num'] = 3
        self.data_frame_ans['temperature']['bytes'] = []
        self.data_frame_ans['temperature']['value'] = 0
        self.data_frame_ans['temperature']['convert'] = self.convert_temp_ans_to_num

        self.data_frame_ans['voltage_status']['word_msb'] = 0b101 << 5
        self.data_frame_ans['voltage_status']['item_num'] = 4
        self.data_frame_ans['voltage_status']['item_list'] = ['under_voltage', 'over_voltage', 'optical_trans_1',
                                                              'optical_trans_2']
        self.data_frame_ans['voltage_status']['offset'] = [0, 1, 2, 3, 4]
        self.data_frame_ans['voltage_status']['word_num'] = 1
        self.data_frame_ans['voltage_status']['bytes'] = []
        self.data_frame_ans['voltage_status']['value'] = [0, 0, 0, 0, 0]

        self.data_frame_ans['io_status']['word_msb'] = 0b101 << 5
        self.data_frame_ans['io_status']['item_num'] = 4
        self.data_frame_ans['io_status']['item_list'] = ['light_pulse', 'trigger_out', 'fiber_1', 'fiber_2']
        self.data_frame_ans['io_status']['offset'] = [0, 1, 2, 3]
        self.data_frame_ans['io_status']['word_num'] = 1
        self.data_frame_ans['io_status']['bytes'] = []
        self.data_frame_ans['io_status']['value'] = [0, 0, 0, 0, 0]

        self.data_frame_ans['product_number']['word_msb'] = 0b110 << 5
        self.data_frame_ans['product_number']['word_id'] = ['msb', 'lsb']
        self.data_frame_ans['product_number']['offset_msb'] = 5
        self.data_frame_ans['product_number']['offset_lsb'] = 0
        self.data_frame_ans['product_number']['word_num'] = 2
        self.data_frame_ans['product_number']['bytes'] = []
        self.data_frame_ans['product_number']['value'] = 0

        self.data_frame_ans['code_product']['word_num'] = 1
        self.data_frame_ans['code_product']['word_id'] = ['lsb']
        self.data_frame_ans['code_product']['offset_lsb'] = 0
        self.data_frame_ans['code_product']['bytes'] = []
        self.data_frame_ans['code_product']['value'] = 0

        self.data_frame_ans['cr']['word_num'] = 1
        self.data_frame_ans['cr']['word_id'] = ['lsb']
        self.data_frame_ans['cr']['offset_lsb'] = 0
        self.data_frame_ans['cr']['bytes'] = []
        self.data_frame_ans['cr']['value'] = 0

        self.data_frame_ans['lf']['word_num'] = 1
        self.data_frame_ans['lf']['word_id'] = ['lsb']
        self.data_frame_ans['lf']['offset_lsb'] = 0
        self.data_frame_ans['lf']['bytes'] = []
        self.data_frame_ans['lf']['value'] = 0

    def connect_flasher(self, flash_add, flash_host):
        """
        Open socket for TCP/IP client
        :param flash_add: ip address of the flasher (129.194.52.90)
        :param flash_host: host port (default = 50001)
        :return:
        """
        try:
            self.socket_flasher = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket_flasher.connect((flash_add, flash_host))
            return 1
        except Exception as e:
            print("something's wrong with %s:%d. Exception is %s" % (str(self.address), int(self.host), e))
            return 0

    def close_connect_flasher(self):
        """
        Close socket for TCP/IP connection
        :return:
        """
        self.socket_flasher.close()

    def get_flasher_status(self):
        """
        Get the flasher status
        :return:
        """
        self.socket_flasher.send(bytes(self.cmd_status))
        return 'done'

    def start_flasher(self):
        """
        start the flasher
        :return:
        """
        self.socket_flasher.send(bytes(self.cmd_start))
        return 'done'

    def stop_flasher(self):
        """
        Stop the flasher
        :return:
        """
        self.socket_flasher.send(bytes(self.cmd_stop))
        return 'done'

    def reset_flasher(self):
        """
        Reset the flasher
        :return:
        """
        self.socket_flasher.send(bytes(self.cmd_reset))

    def convert_freq_ans_to_num(self):
        """
        Convert answer from flasher to frequency value in Hz
        :return:
        """
        try:
            return int(float(1e10) / 625.0 / float(self.data_frame_ans['pulse_frequency']['value']))
        except ZeroDivisionError:
            return 0

    def convert_volt_ans_to_num(self):
        """
        Convert answer from flasher to voltage value in Volt
        :return:
        """
        return (self.data_frame_ans['led_voltage']['value'] / (3.3 / 1023) * -12.5) - 0.2

    def convert_temp_ans_to_num(self):
        """
        Convert answer from flasher to voltage value in degree celsius
        :return:
        """
        sign = 1
        sign_bit = self.data_frame_ans['temperature']['value'] & (0b1 << 12) >> 12
        if sign_bit == 1:
            sign = -1
        return sign * (self.data_frame_ans['temperature']['value'] & 4095) * 0.0625

    def init_request(self):
        for i, tag in enumerate(['led_status', 'led_voltage', 'pulse_duration', 'pulse_frequency', 'freq_divider',
                                 'pulse_width', 'io_status']):
            for j, val in enumerate(self.data_frame_req[tag]['bytes']):
                self.data_frame_req[tag]['bytes'][j] = self.data_frame_req[tag]['word_msb']

    '''
    For all the change functions the principle is the following:
    We use bitwise manipulation to extract from the integer value the different components: e.g. msb or lsb
    Having extracted these subparts, we build the data word to be sent.
    For instance for the led voltage, we get a 10 bits integer. We need to extract the msb and lsb and send them in two
    different data word with the proper msb mask:
    - If the voltage set is 12.5 V, we get 517 i.e 0b1000000101 (see formula below)
    - For each significant bit correspond a different offset which is used to extract and build the bit words
    a. We apply the mask to get the msb (0b11111 << offset = 0b1111100000): 0b1000000101 & 0b1111100000 = 0b1000000000
    b. Then we shift the bits to the right by the same amount of the offset : 0b1000000000 >> 5 = 0b10000
    c. Finally we do an OR with the word mask: (0b010 << 5 =) 0b01000000 | 0b10000 = 0b01010000
    '''

    def change_led_status(self, new_led_status):
        """
        Change the status (ON/OFF) of LED
        :param new_led_status:
        :return:
        """
        for i in range(13):
            self.data_frame_req['led_status']['bytes'][self.data_frame_req['led_status']['frame_num'][i]] |= \
                new_led_status[self.data_frame_req['led_status']['led_order'][i] - 1] << self.data_frame_ans[
                    'led_status']['offset'][i]

    def change_led_voltage(self, new_led_voltage):
        """
        Change the led voltage
        :param new_led_voltage: new voltage in [7.5, 16.5] V
        :return:
        """
        led_voltage = int((new_led_voltage - 7.9) / (8.44 / 950))
        for i, tag in enumerate(['msb', 'lsb']):
            self.data_frame_req['led_voltage']['bytes'][i] |= self.data_frame_req['led_voltage']['word_msb'] | \
                                                              ((led_voltage & self.mask << self.data_frame_req[
                                                                  'led_voltage']['offset_' + tag]) >>
                                                               self.data_frame_req['led_voltage']['offset_' + tag])

    def change_pulse_duration(self, new_pulse_duration):
        """
        Change pulse duration
        :param new_pulse_duration: pulse duration to be multiplied by 0.1 ns
        :return:
        """
        for i, tag in enumerate(['msb', 'lsb']):
            self.data_frame_req['pulse_duration']['bytes'][i] |= self.data_frame_req['pulse_duration']['word_msb'] \
                                                                 | ((new_pulse_duration & self.mask <<
                                                                     self.data_frame_req['pulse_duration'][
                                                                         'offset_' + tag]) >>
                                                                    self.data_frame_req['pulse_duration'][
                                                                        'offset_' + tag])

    def change_pulse_frequency(self, new_pulse_frequency):
        """
        Change pulse frequency
        :param new_pulse_frequency: frequency in Hz
        :return:
        """
        try:
            new_pulse_frequency = int(float(1e10) / float(new_pulse_frequency) / 625.0)
        except ZeroDivisionError:
            new_pulse_frequency = 0

        for i, tag in enumerate(['msb', 'cmsb', 'clsb', 'lsb']):
            self.data_frame_req['pulse_frequency']['bytes'][i] |= self.data_frame_req['pulse_frequency'][
                                                                      'word_msb'] | \
                                                                  ((new_pulse_frequency & self.mask <<
                                                                    self.data_frame_req['pulse_frequency'][
                                                                        'offset_' + tag]) >>
                                                                   self.data_frame_req['pulse_frequency'][
                                                                       'offset_' + tag])

    def change_freq_divider(self, new_freq_divider):
        """
        Change frequency divider allowing to reach low frequency
        :param new_freq_divider: frequency is divided by this amount
        :return:
        """
        for i, tag in enumerate(['msb', 'csb', 'lsb']):
            self.data_frame_req['freq_divider']['bytes'][i] |= self.data_frame_req['freq_divider']['word_msb'] \
                                                               | ((new_freq_divider & self.mask <<
                                                                   self.data_frame_req['freq_divider'][
                                                                       'offset_' + tag]) >> self.data_frame_req[
                                                                      'freq_divider']['offset_' + tag])

    def change_pulse_width(self, new_pulse_width):
        """
        Change pulse width that commands the LED
        :param new_pulse_width:
        :return:
        """
        for i, tag in enumerate(['msb', 'lsb']):
            self.data_frame_req['pulse_width']['bytes'][i] |= self.data_frame_req['pulse_width']['word_msb'] | \
                                                              ((new_pulse_width & self.mask <<
                                                                self.data_frame_req['pulse_width'][
                                                                    'offset_' + tag]) >>
                                                               self.data_frame_req['pulse_width']['offset_' + tag])

    def change_io_status(self, new_io_status):
        """
        Change status of trigger output and input
        :param new_io_status:
        :return:
        """
        for i, tag in enumerate(['light_pulse', 'trigger_out', 'fiber_1', 'fiber_2']):
            self.data_frame_req['io_status']['bytes'][0] |= new_io_status[i] << self.data_frame_ans['io_status'][
                'offset'][i]

    def send_new_config(self):
        """
        Send new values for all parameters
        :return:
        """
        data_req = []
        for i, tag in enumerate(['led_status', 'led_voltage', 'pulse_duration', 'pulse_frequency', 'freq_divider',
                                 'pulse_width', 'io_status', 'code_product', 'cr', 'lf']):
            for ind, j in enumerate(self.data_frame_req[tag]['bytes']):
                data_req.append(j)
                # print(tag, '\t', bin(j))

        self.socket_flasher.send(bytearray(data_req))
        data_ans = list(self.socket_flasher.recv(self.buffer_size))
        data_ans += list(self.socket_flasher.recv(self.buffer_size))
        self.get_new_config(data_ans)

    def get_new_config(self, data_ans):
        """
        Retreive config after command was sent
        :param data_ans:
        :return:
        """
        cnt = 0

        for i, tag in enumerate(['led_status', 'led_voltage', 'pulse_duration', 'pulse_frequency', 'freq_divider',
                                 'pulse_width', 'temperature', 'voltage_status', 'io_status', 'code_product',
                                 'product_number', 'cr', 'lf']):

            # Reinitialize all values to 0
            if (tag == 'led_status') or (tag == 'voltage_status') or (tag == 'io_status'):
                for j in range(self.data_frame_ans[tag]['item_num']):
                    self.data_frame_ans[tag]['value'][j] = 0
                    self.data_frame_ans[tag]['bytes'] = []
            else:
                self.data_frame_ans[tag]['value'] = 0
                self.data_frame_ans[tag]['bytes'] = []

            for j in range(self.data_frame_ans[tag]['word_num']):
                self.data_frame_ans[tag]['bytes'].append(data_ans[cnt])
                print(bin(data_ans[cnt]))
                cnt += 1
                if (tag == 'led_status') or (tag == 'voltage_status') or (tag == 'io_status'):
                    for k in range(5):
                        self.data_frame_ans[tag]['value'][k + 5 * j] = int((self.data_frame_ans[tag]['bytes'][j]
                                                                            & 0b1 << k) >> k)
                else:
                    self.data_frame_ans[tag]['value'] += int((self.data_frame_ans[tag]['bytes'][j] & self.mask) << \
                                                             self.data_frame_ans[tag][
                                                                 'offset_' + self.data_frame_ans[tag][
                                                                     'word_id'][j]])
