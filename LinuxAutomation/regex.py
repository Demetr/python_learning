import re

cc_list = '''Ether Koenig <ekoenig@vpwk.com>,
    Jerry Batman <jerryb@vpwk.com>,
    Chris Tomson <ctomson@vpwk.com,
    Bobbi Baio <bbaio@vpwk.com'''
re.search(r'Chris', cc_list)
if re.search(r'Chris', cc_list):
    print('found Chris')
# the .group() method returns the actual content matched by the regular expression
matchObject = re.search(r'[R,B]obb[i,y]', cc_list)
if matchObject:
    print(f'found {matchObject.group()}') #he .group() method returns the actual content matched by the regular expression

# ----Character sets----
re.search(r'Jerry', cc_list)
if re.search(r'Jerry', cc_list):
    print('found Jerry')
# the .group() method returns the actual content matched by the regular expression
matchObject = re.search(r'[R,B]obb[i,y]', cc_list)
if matchObject:
    print(f'found {matchObject.group()}')

matchObject = re.search(r'Chr[a-z][a-z]', cc_list)
if matchObject:
    print(f'found {matchObject.group()}')

matchObject = re.search(r'Chronos', cc_list)
print(matchObject)
print(type(matchObject))

print(re.search(r'[A-Za-z]+', cc_list))
# <re.Match object; span=(0, 6), match='Ether'>
print(re.search(r'[A-Za-z]{6}', cc_list))
# <re.Match object; span=(0, 6), match='Koenig'>

# naive email address regex
print(re.search(r'[A-Za-z]+@[a-z]+\.[a-z]+', cc_list))
# <re.Match object; span=(15, 31), match='ekoenig@vpwk.com'> 
      
# production ready email address regex for single email string
email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
print(re.match(email_regex, cc_list))

# Test the regex
test_email = "test@example.com"
if re.match(email_regex, test_email):
    print("Valid email")
else:
    print("Invalid email")

# ----Character classes----
    
charClasses = re.search(r'\w+', cc_list)
print(charClasses)

# production not ready email address regex for single email string
# with character classes but with restricted underscore added to domain and ccTLD
email_regex_with_char_classes_wrong = r"(^[\w.+]+@[\w-]+\.[\w.-]+$)"
print(re.match(email_regex_with_char_classes_wrong, cc_list))

# production ready email address regex with character classes
# with underscore added to domain and ccTLD
email_regex_with_char_classes = r"([\w.+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
print(re.match(email_regex_with_char_classes, cc_list))

# Test the regex
test_email = "test@example.com"
if re.match(email_regex_with_char_classes, test_email):
    print("Valid email")
else:
    print("Invalid email")
print("prod ready regex with_char_classes")
print(re.findall(email_regex_with_char_classes, cc_list))

# ----Named Groups----
# SLD = a Second-Level Domain ccTLD = a Country Code Top-Level Domain
matched = re.search(r'(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<ccTLD>\w+)', cc_list)
matched.group('name')
print(f'''name: {matched.group("name")}
Secondary Level Domain: {matched.group("SLD")} ... Top Level Domain: {matched.group("TLD")}''')

# ----Anchors----
# TODO: other regex examples