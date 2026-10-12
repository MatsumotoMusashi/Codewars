def to_camel_case(text):
    if text != '':
        new = []
        for a in text.split('-'):
            for b in a.split('_'):
                new.append(b)
        want = []
        for c in range(len(new)):
            if c == 0:
                want.append(new[c][0] + new[c][1*int(2 <= len(new[c])):].lower()*int(2 <= len(new[c])))
            else:
                want.append(new[c][0].upper() + new[c][1*int(2 <= len(new[c])):].lower()*int(2 <= len(new[c])))
        return ''.join(want)
    else:
        return ''