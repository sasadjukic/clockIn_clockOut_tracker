
from datetime import datetime 

employees = {}

def display_welcome_message(employee: str, time: str) -> None:
    print(f'\nWelcome {employee}')
    print(f"You clocked-in at {time}")

def display_goodbye(employee: str, clock_in: str, clock_out: str, decimal_shift: int) -> None:
    print(f'\nGoodbye {employee}')
    print(f"Clocked-in at {clock_in}")
    print(f"Clocked-out at {clock_out}")
    print(f'Hours worked: {decimal_shift}')

def convert_time_to_decimal(shift: datetime) -> int:
    hours_minutes = str(shift).split(' ')[1].split(':')
    hours = hours_minutes[0]
    minutes = hours_minutes[1]
    prep_decimal = int(hours) * 60 + int(minutes)

    return prep_decimal

def find_decimal_shift_length(clock_out: int, clock_in: int) -> float:
    return round((clock_out - clock_in) / 60, 2)

def configure_time(time: datetime) -> str:
    return str(time).split('.')[0]


def main():
    try:
        while True:
            name = input('\nYour name: ')
            dt = datetime.now()
            clock_in = convert_time_to_decimal(dt)

            if not name in employees:
                employees.setdefault(name, [configure_time(dt), clock_in])
                display_welcome_message(name, configure_time(dt))
            else:
                clock_out = convert_time_to_decimal(dt)
                shift_decimal = find_decimal_shift_length(clock_out, employees[name][1])
                display_goodbye(name, employees[name][0], configure_time(dt), shift_decimal)
                employees.pop(name)

    except KeyboardInterrupt:
        print('\nDone')

if __name__ == '__main__':
    main()
