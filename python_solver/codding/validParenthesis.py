def isValid(s: str) -> bool:        
    m_list = []
    reverse = {
        ')' : '(',
        '}' : '{' ,
        ']' : '['
    }
    for i in s:
        if i == '(' or i=='{' or i=='[':
            m_list.append(i)
        else:
            if len(m_list)>0 and m_list[len(m_list)-1] == reverse[i]:
                m_list.pop()
            else:
                m_list.append(i)

    if len(m_list)<1:  
        return True
    else:
        return False
    
