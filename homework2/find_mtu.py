import subprocess

def ping(host, packet_size):
    """
    Ping a host with a specified packet size.
    
    Args:
    - host (str): The target host to ping.
    - packet_size (int): The size of the packet to send.

    Returns:
    - bool: True if the ping was successful, False otherwise.
    """
    try:
        result = subprocess.run(
                    ['ping', host, '-c', '1', '-M', 'do', '-s', str(packet_size)], 
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
        return result.returncode == 0
    except Exception as e:
        print(f'Произошла критическая ошибка: {e}')
        exit(1)


def main():
    target_host = input('Введите имя или IP хоста, для которого нужно узнать MTU:\n').strip()

    check_input = subprocess.run(['ping', target_host, '-c', '1'], stdout=subprocess.DEVNULL)
    if check_input.returncode != 0:
        print('Похоже, что введенный вами адрес не существует. Пожалуйста, попробуйте еще раз.')
        return
    
    l = 56
    r = 65537

    while r - l > 1:
        m = (l + r) // 2
        if not ping(target_host, m):
            r = m
        else:
            l = m
    
    print(f'Минимальное MTU по пути к "{target_host}" = {l}')

    



if __name__ == "__main__":
    main()