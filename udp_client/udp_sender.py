import socket


def send_udp_package(udp_ip, udp_port, message):
    """
    Send a message via udp.
    https://wiki.python.org/moin/UdpCommunication

    :param udp_ip:   target ip address
    :param udp_port: target udp port
    :param message:  message to send
    :return: None
    """
    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.sendto(message.encode(), (udp_ip, udp_port))


if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 5005
    message = "Flipdot FTW!"
    send_udp_package(ip, port, message)
