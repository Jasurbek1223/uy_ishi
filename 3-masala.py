try:
    arr =input().split()
    sana = arr[0]
    vaqt = arr[1]
    d = sana.split('.')
    h = vaqt.split(':')
    h[0] = int(h[0])
    h[1] = int(h[1])
    d[0] = int(d[0])
    oy = {  '01':'January',
            '02':'February',
            '03':'March',
            '04':'April',
            '05':'May',
            '06':'Iyun',
            '07':'Iyul',
            '08':'August',
            '09':'September',
            '10':'October',
            '11':'November',
            '12':'December' }

    print(f"{d[0]} {oy[d[1]]} {d[2]} year {h[0]} hours {h[1]} minutes")
except:
    print('Notori malumot kiritildi!')
    