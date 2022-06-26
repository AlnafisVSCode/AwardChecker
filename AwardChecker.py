progress_report = {
    'Progress': 0,
    'Trailing': 0,
    'Retriever': 0,
    'Excluded': 0
}

def check_valid_range(pass_v, defer_v, fail_v):
    valid_range = (0, 20, 40, 60, 80, 100, 120)
    if pass_v not in valid_range or \
        defer_v not in valid_range or \
        fail_v not in valid_range:
        print('Range error')
        return False
    return True

def check_total(pass_v, defer_v, fail_v):
    if pass_v + defer_v + fail_v != 120:
        print('Total incorrect')
        return False
    return True

def display_progress_report():
    count = 0
    for k in progress_report:
        count += progress_report[k]
        print('%s %d: %s' % (k, progress_report[k], '*' * progress_report[k]))
    print(str(count) + ' outcomes in total.')

def check_for_quit(value):
    if value == 'q':
        display_progress_report()
        exit(0)

def main():
    pass_v = input('Pass: ')
    check_for_quit((pass_v))
    defer_v = input('Defer: ')
    check_for_quit(defer_v)
    fail_v = input('Fail: ')
    check_for_quit(fail_v)

    try:
        pass_v = int(pass_v)
        defer_v = int(defer_v)
        fail_v = int(fail_v)
    except ValueError:
        print('Integers required')
        exit(1)

    if not check_valid_range(pass_v, defer_v, fail_v):
        exit(2)

    if not check_total(pass_v, defer_v, fail_v):
        exit(3)

    if pass_v == 120:
        print('Progress')
        progress_report['Progress'] += 1
    elif pass_v == 100:
        print('Progress - module trailer')
        progress_report['Trailing'] += 1
    elif pass_v == 80 or pass_v == 60 or \
        (pass_v == 60 and defer_v >= 20) or (pass_v == 20 and defer_v >= 40) or \
        (pass_v == 0 and defer_v >= 60) or (pass_v == 40 and fail_v <= 60):
        print('Do not progress - module retriever')
        progress_report['Retriever'] += 1
    elif fail_v >= 80:
        print('Exclude')
        progress_report['Excluded'] += 1

while True:
    main()
