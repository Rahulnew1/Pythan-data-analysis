contact={
    'police':'100',
    'ambulamce':'102'
}
while True:
    print('search a contact')
    q= input('>>>')
    if len(q)== 0:
        print('closing donw...')
        break
    if q in contact:
        print(f'{q}:{contact[q]}')
    elif q== 'all':
        print('all contact:')
        for k,v in contact.item():
            print(f'{k}:{v}')
    else:
        print(f'{q} not found')
        print('add new contact?')
        new_contact=input('>>.')
        if len (new_contact)== 0:
            print('skipping...')
        contact[q]=new_contact
        print(f'{q}:{contact[q]}added')
            
