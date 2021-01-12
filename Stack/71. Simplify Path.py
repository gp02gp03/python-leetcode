def simplifyPath(path):
    st = []
    dirs = path.split('/')
    for s in dirs:
        if s == '..':
            if st:
                st.pop()
        elif s != '.' and s != '':
            st.append(s)
    return '/'.join(st)


print(simplifyPath('/home/'))
