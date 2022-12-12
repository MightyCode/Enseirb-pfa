import jack
from time import sleep

SOURCE_GROUP = "PulseAudio JACK Sink"

SOURCE_LEFT = SOURCE_GROUP + ":front-left"
SOURCE_RIGHT = SOURCE_GROUP + ":front-right"

INPUT_FORMAT = "system:playback_"
NB_SPEAKERS = 10


def disconnect_all_ports(client):
    for port in client.get_ports(SOURCE_GROUP + ':', is_output=True):
        for connection in port.get_all_connections():
            client.disconnect(port, connection)


def port_connected(port1: jack.Port, port2: jack.Port):
    print(f"[*] Connected {port1.name} to {port2.name}")


def connect_speaker(client, index, state=(True, True)):
    if state[0]:
        client.connect(SOURCE_LEFT, INPUT_FORMAT + str(index))
    if state[1]:
        client.connect(SOURCE_RIGHT, INPUT_FORMAT + str(index + 10))


def disconnect_speaker(client, index, state=(True, True)):
    if state[0]:
        client.disconnect(SOURCE_LEFT, INPUT_FORMAT + str(index))
    if state[1]:
        client.disconnect(SOURCE_RIGHT, INPUT_FORMAT + str(index + 10))


def disconnect_all_from_outputs(client):
    for port in client.get_ports(SOURCE_GROUP + ':', is_output=True):
        for connection in client.get_all_connections(port):
            client.disconnect(port, connection)


def display_all_inputs(client):
    print("Inputs:")
    for port in client.get_ports(is_physical=True, is_input=True):
        print("\t" + port.name)


def display_all_outputs(client):
    print("Outputs:")
    for port in client.get_ports(is_physical=True, is_output=True):
        print("\t" + port.name)


def display_all_connections(client):
    for port in client.get_ports(is_physical=True, is_output=True):
        print(port.name)
        for connection in client.get_all_connections(port):
            print("\t" + connection.name)


def display_all_ports(client):
    for port in client.get_ports():
        print(port.name)


def circle(client, start=1, end=NB_SPEAKERS, duration=2):
    for i in range(start, end):
        if i != start:
            disconnect_speaker(client, i - 1)

        connect_speaker(client, i)

        sleep(duration)


def connect_all_speakers(client):
    for i in range(1, NB_SPEAKERS):
        connect_speaker(client, i)


def main():
    client_name = "s1ddharthaa"
    client = jack.Client(client_name)

    if client.status.server_started:
        print('[+] JACK server was started')
    else:
        print('[*] JACK server was already running')
    if client.status.name_not_unique:
        print('[-] Name {0!r} already taken'.format(client_name))
        print('[*] Unique name {0!r} assigned'.format(client.name))

    # Activate client
    client.activate()

    # Display all ports
    disconnect_all_from_outputs(client)

    connect_all_speakers(client)

    # End client session
    client.deactivate()
    client.close()


if __name__ == '__main__':
    main()
