scrambled = "ocip{FTC0l_I4_t5m_ll0m_y_y3n5406d06dÿÜ}"

blocks = []
for i in range(0, len(scrambled), 4):
    chunk = scrambled[i:]
    if len(chunk) > 4:
        chunk = chunk[0:4]

    blocks.append(''.join(chunk))

flag = ''
for block in blocks:
    flag = flag + block[::-1]

print(flag)