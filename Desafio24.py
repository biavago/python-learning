city = str(input('Digite o nome da cidade: ')).split()

print('santo' in city[0].lower() or 'santa' in city[0].lower() or 'são' in city[0].lower())

# print(any(s in city[0].lower() for s in ('santo', 'santa', 'são')))
