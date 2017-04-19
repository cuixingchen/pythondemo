#!/usr/bin/python


class HostsUtil:
    env = ''

    def __init__(self):
        self.get_input()

    def get_input(self):
        self.env = input('Enter host mark:').strip()
        self.env = '#' + self.env

    def switch_host(self, file_name):
        line_list = HostsUtil.read_file(file_name)
        new_line_list = []
        require_deal = False
        env_deal = False
        for line in line_list:
            if '_start_' in line:
                require_deal = True
                if self.env == '#' or self.env not in line:
                    env_deal = False
                else:
                    env_deal = True
                new_line_list.append(line)
                continue
            elif '_end_' in line:
                require_deal = False
                new_line_list.append(line)
                continue
            if require_deal:
                if env_deal:
                    line = line.replace('#', '')
                else:
                    if not line.startswith('#'):
                        line = '#' + line
            new_line_list.append(line)
        HostsUtil.write_file(file_name, new_line_list)

    @staticmethod
    def read_file(file_name):
        hosts_input = open(file_name)
        try:
            return hosts_input.readlines()
        finally:
            hosts_input.close()

    @staticmethod
    def write_file(file_name, line_list):
        hosts_input = open(file_name, 'w')
        try:
            for line in line_list:
                hosts_input.writelines(line)
        finally:
            hosts_input.close()


x = HostsUtil()
# x.switch_host('/home/cuipengfei/hosts')
x.switch_host('/etc/hosts')
