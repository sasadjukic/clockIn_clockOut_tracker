
from datetime import datetime 
import time

employees = {}

def display_welcome_message(employee, time) -> None:
    print(f'\nWelcome {employee}')
    print(f"You clocked-in at {str(time).split('.')[0]}")

def display_goodbye(employee, clock_in, clock_out, decimal_shift) -> None:
    print(f'\nGoodbye {employee}')
    print(f"Clocked-in at {str(clock_in).split('.')[0]}")
    print(f"Clocked-out at {str(clock_out).split('.')[0]}")
    print(f'Hours worked: {decimal_shift}')

def find_decimal_time(shift) -> int:
    hours_minutes = str(shift).split(' ')[1].split(':')
    hours = hours_minutes[0]
    minutes = hours_minutes[1]
    prep_decimal = int(hours) * 60 + int(minutes)

    return prep_decimal

def main():
    try:
        while True:
            name = input('\nYour name: ')
            dt = datetime.now()
            clock_in = find_decimal_time(dt)

            if not name in employees:
                employees.setdefault(name, [dt, clock_in])
                display_welcome_message(name, dt)
            else:
                clock_out = find_decimal_time(dt)
                shift_decimal = round((clock_out - employees[name][1]) / 60, 2)
                display_goodbye(name, employees[name][0], dt, shift_decimal)
                employees.pop(name)

    except KeyboardInterrupt:
        print('\nDone')

if __name__ == '__main__':
    main()
