class View():

    def __init__(self):
        pass

    def print_message(self, json_data):
        print("\r{}: {}\n{}: ".format(json_data["username"],
                                      json_data["message"],
                                      end=''))
