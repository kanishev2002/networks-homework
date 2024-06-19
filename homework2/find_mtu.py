import subprocess
import re

def parse_mtu(output: str):
    mtu_line = None
    for line in output.splitlines():
        if 'pmtu' in line:
            mtu_line = line
            break
    
    if mtu_line:
        match = re.search(r'pmtu (\d+)', mtu_line)
        if match:
            mtu = int(match.group(1))
            return mtu

    print("Произошла ошибка. Информация об MTU не найдена.")
    exit(1)


def main():
    target_host = input('Введите имя или IP хоста, для которого нужно узнать MTU:\n').strip()

    check_input = subprocess.run(['ping', target_host, '-c', '1'], stdout=subprocess.DEVNULL)
    if check_input.returncode != 0:
        print('Похоже, что введенный вами адрес не существует. Пожалуйста, попробуйте еще раз.')
        return
    
    try:
        result = subprocess.run(['tracepath', target_host], 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE, 
                                text=True)
        output = result.stdout
        mtu = parse_mtu(output)
        print(f'Минимальное MTU по пути к "{target_host}" = {mtu}')
        
    
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        exit(1)


if __name__ == "__main__":
    main()