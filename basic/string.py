def demo():

    str1 = 'dummy'
    str2 = 'Demo'

    # String
    x = 'String: Demo %s' % str1
    print (x)  # 'Demo dummy'

    # Format
    print ('Format 1:Demo {}'.format(str1)) # Demo dummy

    print ('Format 2:Demo {str1}.'.format(str1='dummy')) #Demo dummy.

    print ('Format 3:Demo {:10s}.'.format('dummy')) #Demo dummy      .


    # f-string 
    #    end with = to print label
    print (f'f-string {str1} {str2=}') # dummy str2='Demo'


    # Template
 
 #   from string import Template
 #  t = Template('Hello $name')
 #  print( t.substitute(str1=str1))
 