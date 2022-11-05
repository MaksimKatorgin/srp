#!c:/ . . . /python.exe
print("Access-Control-Allow-Origin: *")
print()
import cgi, cgitb, random, pickle
from my_mod import write_results, D
cgitb.enable()
def get_test(file_name):
    f = open(file_name, 'rb')
    test_list=pickle.load(f)
    f.close()
    test = random.choice(test_list)
    test_list.remove(test)
    f = open('cur_tests.dat', 'wb')
    pickle.dump(test_list, f)
    f.close()
    return test

def write_results(user_dict, out_points=0, out_answers=0):
    print('<i><b>Results:</b></i>', '<br>Username &ndash; ', user_dict['name'])
    if out_answers:
        print('<br>Answers &ndash; ')
        for el in user_dict[ 'answers' ]:
            print(el)
    if out_points:
        print('<br>Points &ndash; ', user_dict['points'], ' out of  ', user_dict['number_test'])

max_test=3
ans = ''
data=cgi.parse()
if 'name' in data:
    test=get_test('tests.dat')
    print(test.split(';')[0])
    user_dict = {
        'name' :data['name'][0],
        'number_test' :1,
        'tests' :[test],
        'answers' :[],
        'points' :0}
    f = open('user.dat', 'wb')
    pickle.dump(user_dict, f)
    f.close()
    
if 'answer' in data:
    f = open('user.dat', 'rb')
    user_dict = pickle.load(f)
    user_dict['answers'] += [data['answer'][0]]
    tests = user_dict['tests']
    etalon = tests[len(tests) - 1:][0].split(';')[1]
    if data['answers'][0] == etalon:
        user_dict['points'] += 1
    if user_dict['number_test'] < max_test:
        test = get_test('cur_tests.dat')
        print(D, test.split(';')[0])
        user_dict['number_test'] += 1
        user_dict['tests'] += [test]
        f = open('user.dat', 'wb')
        pickle.dump(user_dict, f)
        f.close()
    else:
        write_results(user_dict, out_points=1, out_answers=1)
