from steganography.steganography import Steganography

print'WELCOME SPY'
spyfriend_list = ['james', 'bond']
spy_msg=[]
secret_text=[]
spy_name='spy1'
print'your default name is ' + spy_name
spy_name_change_input=raw_input('press y to change name and n to continue with default name(y/n)')
if spy_name_change_input== 'y':

    print 'enter new name'
    spy_name=raw_input('')
    print'your new name is ' + spy_name
else:
    print' your name is ' + spy_name
spy_age=int(raw_input('enter your age(limit 12-50)'))
if spy_age<11:
 print('invalid user')
 quit()
if spy_age>51:
   print('invalid user')
else:
    print ('valid user ' )
spy_address=raw_input('enter your address')
(spy_rating)=1
spy_gender=raw_input('what is your gender\npress m for male & f for female (m/f)')
if spy_gender=='m':
    print ('HELLO MR.' + spy_name +' ' + 'your age is '+ str( spy_age ) + ' of ' + spy_address  + ' rating = ' + str( spy_rating))
elif spy_gender=='f':
    print ('HELLO MS.'+ spy_name +' ' +  'your age is '+str( spy_age ) + ' of ' + spy_address + ' rating = ' + str( spy_rating) )
else:
    print('please specify your gender')
    quit()
while True:
    print'press 1. to you add status'
    print'press 2. to add a friend'
    print'press 3. to send an encoded message'
    print'press 4. to read message'
    print'press 5. to read chat history'
    print'prrss 6. to exit'
    choice = int(raw_input('enter choice(1/2/3/4/5/6) : '))
    if choice==1:
        print 'press 1. to enter a new status'
        print 'press 2. to use existing status'
        spy_status_choice=int(raw_input('1. or 2.'))
        spy_status = ['good morning', 'happy', 'sad', "can't talk spy chat only", 'at the gym']
        if spy_status_choice==1:
            spy_stat=raw_input('enter status ')
            spy_status.append(spy_stat)
            print'your new status is ' + spy_stat
            print spy_status
        else:
            print 'select existing status'
            #spy_status = ['good morning', 'happy', 'sad', "can't talk spy chat only", 'at the gym']
            print'existing status are '
        spy_exist_status= int(raw_input(" 1.good morning \n 2.happy \n 3.sad \n 4.can't talk spy chat only \n 5.at the gym"))
        if spy_exist_status == 1:
         print 'your status is ' + str(spy_status[0])
        elif spy_exist_status==2:
         print 'your status is ' + str(spy_status[1])
        elif spy_exist_status==3:
         print 'your status is ' + str(spy_status[2])
        elif spy_exist_status==4:
         print 'your status is ' + str(spy_status[3])
        elif spy_exist_status==5:
         print 'your status is ' + str(spy_status[4])
        else:
         spy_new_status=raw_input('status can not be blank\nenter some status')
         print ('your status is ' + spy_new_status)
    if choice==2:
        spyfriend_list = ['james', 'bond']
        spy_friend_dict={
            'spy_friend1':{
              'name':'james',
              'age':26,
              'rating':2
            },
         'spy_friend2':{
            'name':'bond',
            'age':30,
            'rating':3.5
         }
        }
        print'enter the details of the friend you want to add'
        spy_friend_name=raw_input("enter friend's name")
        if spy_friend_name=='':
         print'invalid name'
        spy_friend_age=int(raw_input("enter friend's age between 12-50"))
        if spy_friend_age < 11:
         print('invalid age')
        elif spy_friend_age>51 :
          print 'invalid age'
        spy_friend_rating=float(raw_input('enter the rating of your spy friend'))
        if spy_friend_rating>spy_rating:
         spyfriend_list.append(spy_friend_name)
         spy_friend_dict.update({'Rating': spy_friend_rating})
         spy_friend_dict.update({'Age': spy_friend_age})
         spy_friend_dict.update({'Name': spy_friend_name})
        else:
            print 'spy rating too low'
        print'your friends are ' + str(spy_friend_dict)
        #spy_menu()
    if choice==3:
        spy_msg=[]
        secret_text=[]
        select_a_friend = raw_input('\nSelect the name of your friend whom you want to '
                                                            'send a secret message: \n')
        if select_a_friend in spyfriend_list:
            print 'Index of Selected Friend is: ' + spyfriend_list.index()
            spy_img_path = raw_input('Enter the path to the image to which you want to encode your message')
            spy_text = raw_input('Enter your Secret Message : ')
            spy_hidden_img = raw_input('Enter the final image name with .png EXTENTION ')
            Steganography.encode(spy_img_path, spy_hidden_img, spy_text)  # Steganography for encoding the image
            secret_text = Steganography.decode(spy_hidden_img)  # Store in the image
            spy_msg.append(secret_text)

        else:
            print select_a_friend + ', is not present in your friend list'
            spyfriend_list.append(select_a_friend)
            print str(spyfriend_list) + '\nNew Friend added to the list, index is: ' + str(spyfriend_list.index(select_a_friend))
            spy_img_path = raw_input('\nEnter the path to the image to which you want to encode your message')
            spy_text = raw_input('Enter a Secret Message ')
            spy_hidden_img = raw_input('Enter the final image name with .png EXTENTION ')
            Steganography.encode(spy_img_path, spy_hidden_img, spy_text)
            secret_text = Steganography.decode(spy_hidden_img)
            spy_msg.append(secret_text)

    if choice==4:
         if spy_msg=='':
             print 'No Message Received \n'
    else:
            print 'Your Secret Message is: \n' + str(spy_msg)
    if choice==5:
         if spy_msg=='':
             print 'No Chat History \n'
    else:
        select_a_friend=raw_input('enter your friends name')
        if select_a_friend:
              print 'You Contacted ' + str(select_a_friend) + ' and you sent him ' + str(secret_text)
    if choice==6:
        break

