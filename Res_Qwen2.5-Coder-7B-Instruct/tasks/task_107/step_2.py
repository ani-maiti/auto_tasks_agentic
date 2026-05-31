import dns.resolver

answers = dns.resolver.resolve('wikipedia.org', 'A')
for answer in answers:
    print(answer.address)