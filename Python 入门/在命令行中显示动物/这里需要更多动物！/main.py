camel = r"""
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
"""
dolphin = r"""
                                   __
                               _.-~  )
                    _..--~~~~,'   ,-/     _
                 .-'. . . .'   ,-','    ,' )
               ,'. . . _   ,--~,-'__..-'  ,'
             ,'. . .  (@)' ---~~~~      ,'
            /. . . . '~~             ,-'
           /. . . . .             ,-'
          ; . . . .  - .        ,'
         : . . . .       _     /
        . . . . .          `-.:
       . . . ./  - .          )
      .  . . |  _____..---.._/ _____
~---~~~~----~~~~             ~~~~----~~~~
"""
elephant = r"""
                            _.-----.._____,-~~~~-._...__
                         ,-'            /         `....
                       ,'             ,'      .  .  \::.
                     ,'        . ''    :     . \  `./::..
                   ,'    ..   .     .      .  . : ;':::.
                  /     :go. :       . :    \ : ;'.::.
                  |     ' .o8)     .  :|    : ,'. .
                 /     :   ~:'  . '   :/  . :/. .
                /       ,  '          |   : /. .
               /       ,              |   ./.
               L._    .       ,' .:.  /  ,'.
              /-.     :.--._,-'~~~~~~| ,'|:
             ,--.    /   .:/         |/::| `.
             |-.    /   .;'      .-__)::/    \
...._____...-|-.  ,'  .;'      .' '.'|;'      |
  ~--..._____\-_-'  .:'      .'   /  '
   ___....--~~   _.-' `.___.'   ./
     ~~------+~~_. .    ~~    .,'
                 ~:_.' . . ._:'
                    ~~-+-+~~
"""
panda = r'''
                     ooo
                  o$$$$$$          o$$$$$o             ooo
                 $$$$$$"""""""""$o$$$$$$$$oo"""""""o o$$$$$$o
                  ""$             $$$$$"            $$$$$$$$$
                   $                $                 $$$$$$$
                 o ooooo                               "$$$"
               o  $$$o$$   o$$o   o" ooo                "$
               $   """    "$ o$$ o o$" $    $$"$$$      
               o     ooo    ""$"  o"$$"      "$$$$$      $
           oo$$$"" "o "$""         "    o      """     oo"
         o$$$$o        """"oo$$$$oo"$ $"$"  o     o"$$$$
       o$$$$$$$$"$$$$$$$$$$$$$$$$$ $$$o$""""          "$$$
       $$$$$$$$$o$$$$$$$$$$$$$$$$$o$$$$$$$o             $$$$
       $$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$o     oo$$$$$$$$o
      o$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$oo$$$$$$$$$$$$
   o$$$$$o"$$$$"          "$$$""  $$$$$$$$$$$$$$o"$$$$$$$$$""o
 o$$$$$$$                          "$$$$$$$$$$$$$$o"$$$$$"     $$o    ooo
 $$$$$$$$                        $     "$$$$$$$$$$$$           $$$$$o$$$$$
 $$$$$$$$o              ooo$$$$$$$         """""""$"          $$$$$$$$$$$"
  $$$$$$$$   o$$$$$$$$$$$$$$$$$$$$o   oo$$$$$$$$$o     o$$$$$ $$$$$$$$$$$
   $$$$$$$"o$$$$$$$$$$$$$$$$$$$$$$$oo$$$$$$$$$$$$$$$$$$$$$$$$$o$$$$$$$$"
   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""
 $$$$$$$$ $$$$$$$$$$$$$$$$$$$$$$$$"    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 "$$$$"" $$$$$$$$"""$$$$$$""""           "$$$$$$$$$$$$$$$$$""$$$$$"
          $$$$$"                              """"$$$$$""
'''
zoo_dict = {'camel': camel, 'elephant': elephant, 'panda': panda, 'dolphin': dolphin}

print('Camel:' + zoo_dict['camel'])
print('Elephant:' + zoo_dict['elephant'])
print('Panda:' + zoo_dict['panda'])
print('Dolphin:' + zoo_dict['dolphin'])

# 如果我想知道 zoo 中有哪些动物，我需要怎么办呢？
print(zoo_dict.keys())

# 现在，我想把 兔子 添加进去，怎么办？
rabbit = r'''
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \
\//\/      .- \
 Y        /    Y
 l       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )
'''
zoo_dict['rabbit'] = rabbit
print(zoo_dict['rabbit'])
