



###############################################################################################
#---------------------------------------------------------------------------------------------#
#                    Desarrollado por Luis Saucedo Mora, ETSIAE. 
#---------------------------------------------------------------------------------------------#
###############################################################################################

#---------------------------------------------------------------------------------------------#
#                                    Verificador para el ejercicio de RME
#---------------------------------------------------------------------------------------------#

#       Version 0

# el texto no tiene tildes porque en algunos compiladores da error

import math

print('')
print('###################################################################################################')
print('')
print('                              Verificador para el ejercicio de RME.  GIA                                ')
print('')
print('                 El texto no tiene tildes porque en algunos compiladores da error')
print('')
print('                                                 Version BETA')
print('')



error_index=0 # si esto es 1, no sigue el código
error_global=10.0 
fact_round=0.005


try:
    error_index=3
    # Cargar datos personales

    ## HERE en grupo o individual, imprimir todos los nombres
    
    fcell= open('datos_personales.txt','r')
    ind=0
    componentes=0
    for line in fcell.readlines() :
        vecaux=[str(x) for x in line.split()]
        if ind>0:
            if len(vecaux)!=7:
                print('->  |||||| ERROR EN datos_personales.txt ||||||  ')
                print('La fila ',int(ind) , ' esta incompleta o sobran elementos, hay que corregirlo y volver a ejecutar el programa.')
                error_index=1
            else:
                name=vecaux[0]
                surname1=vecaux[1]
                surname2=vecaux[2]
                DNI_num=int(vecaux[3])
                DNI_letra=vecaux[4]
                grupo=vecaux[5]
                mail=vecaux[6]
                error_index=0
                print('')
                print('DATOS PERSONALES:')
                print('')
                print('Nombre: ', name, surname1, surname2)
                print('DNI: ', DNI_num, '-',DNI_letra )
                print('Grupo administrativo: ', grupo)
                print('e-mail: ', mail)
                print('')
                componentes+=1
        
        ind+=1
    fcell.close()

    if error_index!=3:
        print('')
        if componentes>1:
            print('')
            print('TRABAJO EN GRUPO DE ', componentes)
            print('')
            print('Los datos personales del ultimo componente seran usados para identificar el trabajo:')
        else:
            print('')
            print('TRABAJO INDIVIDUAL')
            
        print('')
        print('DATOS PERSONALES:')
        print('')
        print('Nombre: ', name, surname1, surname2)
        print('DNI: ', DNI_num, '-',DNI_letra )
        print('Grupo administrativo: ', grupo)
        print('e-mail: ', mail)
        print('')
        ### copiar datos personales
##
##        fcell= open('datos_personales.txt','r')
##        ff= open('datos_personales_'+name+'_'+surname1+'_'+surname2+'.txt','w')
##        for line in fcell.readlines() :
##            vecaux=[str(x) for x in line.split()]
##            for m in range(0,len(vecaux)):
##                ff.write(vecaux[m])
##                ff.write(' ')
##            ff.write('\n')
##        ff.close
##        fcell.close()
    else:
        print('->  |||||| ERROR   Revise los datos personales y complete el archivo correctamente ||||||  ')
    
except IOError:
    print('Como primer paso, es necesario crear y rellenar adecuadamente los datos personales.')
    print('el archivo datos_personales.txt no existe y se ha creado en blanco para que sea rellenado.')
    fcell= open('datos_personales.txt','w')
    fcell.close()
    error_index=3


Young=200000.0
Alpha=125*pow(10,-7)
# Cargar datos cargas
if error_index!=3:
    try:  
        fcell= open('cargas_'+name+'_'+surname1+'_'+surname2+'.txt','r')
        loads=[]
        ind=0
        carga_termica=0
        carga_p=0
        carga_torsor=0
        for line in fcell.readlines() :
            vecaux=[str(x) for x in line.split()]
            if ind>0:
                if len(vecaux)!=16:
                    print('->  |||||| ERROR EN '+ 'cargas_'+name+'_'+surname1+'_'+surname2+'.txt'' ||||||')
                    print('La fila ',int(ind) , ' esta incompleta o sobran elementos, hay que corregirlo y volver a ejecutar el programa.')
                    error_index=1
                else:
                    if int(vecaux[1])!=int(ind):
                        print('->  |||||| ERROR EN '+ 'cargas_'+name+'_'+surname1+'_'+surname2+'.txt'' ||||||')
                        print('La fila ', int(ind) , ' esta mal numerada, hay que corregirlo y volver a ejecutar el programa.')
                        error_index=1
                    loads_loc=[vecaux[0]]
                    for i in range(1,len(vecaux),1):
                        loads_loc.append(float(vecaux[i]))
                    loads.append(loads_loc)
                    if loads_loc[2]==4: carga_termica+=1
                    if loads_loc[2]==3: carga_torsor+=1
                    if loads_loc[2]<3: carga_p+=1
                    
            ind+=1
        fcell.close()
        
    except IOError:
        print('El archivo para introducir las cargas no existe y se creara en blanco para rellenarlo con los datos del excel.')
        fcell= open('cargas_'+name+'_'+surname1+'_'+surname2+'.txt','w')
        fcell.close()
        error_index=2

# Cargar datos apoyos
if error_index!=3:
    try:  
        fcell= open('apoyos_'+name+'_'+surname1+'_'+surname2+'.txt','r')
        supports=[]
        supports_connect=[]
        ind=0
        for line in fcell.readlines() :
            vecaux=[str(x) for x in line.split()]
            if ind>0:
                if len(vecaux)!=9:
                    print('->  |||||| ERROR EN '+'apoyos_'+name+'_'+surname1+'_'+surname2+'.txt'' |||||| ')
                    print('La fila ',int(ind) , ' esta incompleta o sobran elementos, hay que corregirlo y volver a ejecutar el programa.')
                    error_index=1
                else:
                    if int(vecaux[1])!=int(ind):
                        print('->  |||||| ERROR EN '+ 'apoyos_'+name+'_'+surname1+'_'+surname2+'.txt'' ||||||')
                        print('La fila ', int(ind) , ' esta mal numerada, hay que corregirlo y volver a ejecutar el programa.')
                        error_index=1
                    supports_loc=[vecaux[0]]
                    for i in range(1,len(vecaux),1):
                        supports_loc.append(float(vecaux[i]))
                    supports.append(supports_loc)
                    supports_connect.append([])
            ind+=1
        fcell.close()
    except IOError:
        print('El archivo para introducir los apoyos no existe y se creara en blanco para rellenarlo con los datos del excel.')
        fcell= open('apoyos_'+name+'_'+surname1+'_'+surname2+'.txt','w')
        fcell.close()
        error_index=2
        
# Cargar datos solidos rigidos
if error_index!=3:
    try: 
        fcell= open('solidos_rigidos_'+name+'_'+surname1+'_'+surname2+'.txt','r')
        rigido_connect_forces=[]
        rigids=[]
        ind=0
        for line in fcell.readlines() :
            vecaux=[str(x) for x in line.split()]
            if ind>0:
                if len(vecaux)!=3:
                    print('->  |||||| ERROR EN '+'solidos_rigidos_'+name+'_'+surname1+'_'+surname2+'.txt'' |||||| ')
                    print('La fila ',int(ind) , ' esta incompleta o sobran elementos, hay que corregirlo y volver a ejecutar el programa')
                    error_index=1
                else:
                    if int(vecaux[1])!=int(ind):
                        print('->  |||||| ERROR EN '+ 'solidos_rigidos_'+name+'_'+surname1+'_'+surname2+'.txt'' ||||||')
                        print('La fila ', int(ind) , ' esta mal numerada, hay que corregirlo y volver a ejecutar el programa.')
                        error_index=1
                    rigids_loc=[vecaux[0]]
                    for i in range(1,len(vecaux),1):
                        rigids_loc.append(float(vecaux[i]))
                    rigids.append(rigids_loc)
                    rigido_connect_forces.append([])

            ind+=1
        fcell.close()
    except IOError:
        print('El archivo para introducir los solidos no existe y se creara en blanco para rellenarlo con los datos del excel.')
        fcell= open('solidos_rigidos_'+name+'_'+surname1+'_'+surname2+'.txt','w')
        fcell.close()
        error_index=2

# Cargar datos nudos
if error_index!=3:
    try: 
        fcell= open('nudos_'+name+'_'+surname1+'_'+surname2+'.txt','r')
        connect_nudos=[]
        nodes=[]
        ind=0
        nudos_barras=0
        nudos_solo=[]
        for line in fcell.readlines() :
            vecaux=[str(x) for x in line.split()]
            if ind>0:
                connect_nudos.append([])
                if len(vecaux)!=5:
                    print('->  |||||| ERROR EN '+'nudos_'+name+'_'+surname1+'_'+surname2+'.txt'' |||||| ')
                    print('La fila ',int(ind) , ' esta incompleta o sobran elementos, hay que corregirlo y volver a ejecutar el programa')
                    error_index=1
                else:
                    if int(vecaux[1])!=int(ind):
                        print('->  |||||| ERROR EN '+ 'nudos_'+name+'_'+surname1+'_'+surname2+'.txt'' ||||||')
                        print('La fila ', int(ind) , ' esta mal numerada, hay que corregirlo y volver a ejecutar el programa.')
                        error_index=1
                    nodes_loc=[vecaux[0]]
                    for i in range(1,len(vecaux),1):
                        nodes_loc.append(float(vecaux[i]))
                    nodes.append(nodes_loc)
                    if nodes_loc[4]!=0 :
                        nudos_barras+=1
                        nudos_solo.append(int(nodes_loc[1]))
            ind+=1
        fcell.close()
    except IOError:
        print('El archivo para introducir los nudos no existe y se creara en blanco para rellenarlo con los datos del excel.')
        fcell= open('nudos_'+name+'_'+surname1+'_'+surname2+'.txt','w')
        fcell.close()
        error_index=2

# Cargar datos barras
if error_index!=3:
    try: 
        fcell= open('barras_'+name+'_'+surname1+'_'+surname2+'.txt','r')
        bars=[]
        ind=0
        baxil=0
        btors=0
        for line in fcell.readlines() :
            vecaux=[str(x) for x in line.split()]
            if ind>0:
                if len(vecaux)!=23:
                    print('->  |||||| ERROR EN '+'barras_'+name+'_'+surname1+'_'+surname2+'.txt'' |||||| ')
                    print('La fila ',int(ind) , ' esta incompleta o sobran elementos, hay que corregirlo y volver a ejecutar el programa')
                    error_index=1
                else:
                    if int(vecaux[11])!=int(0):
                        connect_nudos[int(vecaux[11])-1].append([ind, 0])
                    if int(vecaux[17])!=int(0):
                        connect_nudos[int(vecaux[17])-1].append([ind, 1])
                                                                
                    if int(vecaux[1])!=int(ind):
                        print('->  |||||| ERROR EN '+ 'barras_'+name+'_'+surname1+'_'+surname2+'.txt'' ||||||')
                        print('La fila ', int(ind) , ' esta mal numerada, hay que corregirlo y volver a ejecutar el programa.')
                        error_index=1
                    bars_loc=[vecaux[0]]
                    for i in range(1,len(vecaux),1):
                        bars_loc.append(float(vecaux[i]))
                    bars.append(bars_loc)
                    if bars_loc[2]==1 and abs(bars_loc[3])>0: baxil+=1
                    if bars_loc[2]==2 and abs(bars_loc[3])>0: btors+=1
            ind+=1
        fcell.close()
    except IOError:
        print('El archivo para introducir las barras no existe y se creara en blanco para rellenarlo con los datos del excel.')
        fcell= open('barras_'+name+'_'+surname1+'_'+surname2+'.txt','w')
        fcell.close()
        error_index=2

if error_index!=2 and error_index!=3:
    # comprobar los datos de las barras
    print('')
    print('> Congruency verification of file: '+'barras_'+name+'_'+surname1+'_'+surname2+'.txt')
    print('')

    #       longitud

    print('verificando longitudes ...')
    print('')
    for i in range(0,len(bars),1):
        longloc=pow(pow(bars[i][6]-bars[i][12],2)+pow(bars[i][7]-bars[i][13],2)+pow(bars[i][8]-bars[i][14],2),0.5)
        if abs(bars[i][21]-longloc)/longloc>error_global:
            print('->  |||||| ERROR EN LA BARRA ', bars[i][0], '|||||| , la longitud y la distancia entre inicio y fin no coinciden')
            print('                   Valor calculado= ', round(longloc,3), '  vs  Valor en el fichero=',  round(bars[i][21],3) )
            error_index=1
        else:
            print('        +  Longitud de la barra ', bars[i][0], ' OK')

    print('')
    #       volumen
    print('verificando volumenes ...')
    print('')
    for i in range(0,len(bars),1):
        volloc=bars[i][20]*bars[i][21]
        if abs(bars[i][19]-volloc)/volloc>error_global:
            print('->  |||||| ERROR EN LA BARRA ', bars[i][0], '|||||| , el volumen y A*L no coinciden')
            print('                   Valor calculado= ', round(volloc,3), '  vs  Valor en el fichero=',  round(bars[i][19],3) )
            error_index=1
        else:
            print('        +  Volumen de la barra ', bars[i][0], ' OK')

    print('')

    #       energias
    print('verificando energias ...')
    print('')
    for i in range(0,len(bars),1):
        Eloc=bars[i][3]*bars[i][4]/2.0
        if Eloc==0:
            if bars[i][18]==0:
                print('        ->  La Energia de la barra ', bars[i][0], ' es nula y no trabaja, revisar el archivo o eliminar la barra si no trabaja.')
        else:
            if abs(bars[i][18]-Eloc)/Eloc>error_global:
                print('->  |||||| ERROR EN LA BARRA ', bars[i][0], '|||||| , la energia elastica, el esfuerzo y la deformacion no coinciden')
                print('                   Valor calculado= ', round(Eloc,3), '  vs  Valor en el fichero=',  round(bars[i][18],3) )
                error_index=1
            else:
                print('        +  Energia de la barra ', bars[i][0], ' OK')

    print('')

    #       deformaciones
    print('verificando deformaciones ...')
    print('')
    for i in range(0,len(bars),1):

        if bars[i][2]==1:
            defloc=(bars[i][3]/(bars[i][20]*Young))*bars[i][21]
            if defloc==0:
                if bars[i][4]==0:
                    print('        ->  La Energia de la barra ', bars[i][0], ' es nula y no trabaja, revisar el archivo o eliminar la barra si no trabaja.')
            else: 
                if abs((bars[i][4]-defloc)/defloc)>error_global:
                    print('->  |||||| ERROR EN LA BARRA ', bars[i][0], '|||||| , la deformacion, el esfuerzo y las propiedades no coinciden')
                    print('                   Valor calculado= ', round(defloc,3), '  vs  Valor en el fichero=',  round(bars[i][4],3) )
                    error_index=1
                else:
                    print('        +  Elongacion de la barra ', bars[i][0], ' OK')
                
        if bars[i][2]==2:
            Rloc=pow(bars[i][20]/3.1415,0.5)
            Jloc=bars[i][22]   #3.14*pow(Rloc,4)/2.0 para seccion maciza
            Gloc=(Young)/(2*(1+0.3))
            Philoc=bars[i][3]*bars[i][21]/(Jloc*Gloc)
            if Philoc==0:
                if bars[i][4]==0:
                    print('        ->  La Energia de la barra ', bars[i][0], ' es nula y no trabaja, revisar el archivo o eliminar la barra si no trabaja.')
            else: 

                if abs((bars[i][4]-Philoc)/Philoc)>error_global:
                    print('->  |||||| ERROR EN LA BARRA ', bars[i][0], '|||||| , el giro, el esfuerzo y las propiedades no coinciden')
                    print('                   Valor calculado= ', round(Philoc,3), '  vs  Valor en el fichero=',  round(bars[i][4],3) )
                    error_index=1
                else:
                    print('        +  Giro torsor de la barra ', bars[i][0], ' OK')

        if bars[i][2]!=1 and bars[i][2]!=2:
            print('->  |||||| ERROR EN LA BARRA ', bars[i][0], '|||||| , el esfuerzo no esta bien definido, columna 2')

    print('')
    print('verificando lugar de inicio y final...')
    print('')
    for i in range(0,len(bars),1):    
        if int(bars[i][9]*bars[i][10]+bars[i][9]*bars[i][11]+bars[i][10]*bars[i][11])!=int(0):
            print('->  |||||| ERROR EN LA BARRA ', bars[i][0], '|||||| , tiene mas de un lugar inicial')
            print('              Columnas 10, 11 y 12, valores  ', bars[i][9], bars[i][10], bars[i][11])
            error_index=1
        else:
            print('        +  Lugar inicial de la barra ', bars[i][0], ' OK')
        if int(bars[i][15]*bars[i][16]+bars[i][15]*bars[i][17]+bars[i][16]*bars[i][17])!=int(0):
            print('->  |||||| ERROR EN LA BARRA ', bars[i][0], '|||||| , tiene mas de un lugar final')
            print('              Columnas 16, 17 y 18, valores  ', bars[i][15], bars[i][16], bars[i][17])
            error_index=1
        else:
            print('        +  Lugar final de la barra ', bars[i][0], '   OK')

    #      verificar que es 2D y los torsores ortogonales
    print('')
    print('verificando estructura 2D y barras a torsion ortogonales ...')
    print('') #####
    bars_axil=[]
    bars_tors=[]
    for i in range(0,len(bars),1):
        if bars[i][2]==1:
            bars_axil.append(i)
        if bars[i][2]==2:
            bars_tors.append(i)
        
    if len(bars_axil)>1:
        ind_ref=bars_axil[0]
        vx0=bars[ind_ref][6]-bars[ind_ref][12]
        vy0=bars[ind_ref][7]-bars[ind_ref][13]
        vz0=bars[ind_ref][8]-bars[ind_ref][14]
        longloc=pow(pow(vx0,2)+pow(vy0,2)+pow(vz0,2),0.5)
        vx0*=1.0/longloc
        vy0*=1.0/longloc
        vz0*=1.0/longloc
                
        vec_prod=[]
        for i in range(1,len(bars_axil),1):
            ind_loc=bars_axil[i]
            vx1=bars[ind_loc][6]-bars[ind_loc][12]
            vy1=bars[ind_loc][7]-bars[ind_loc][13]
            vz1=bars[ind_loc][8]-bars[ind_loc][14]
            longloc=pow(pow(vx1,2)+pow(vy1,2)+pow(vz1,2),0.5)
            vx1*=1.0/longloc
            vy1*=1.0/longloc
            vz1*=1.0/longloc

            xvec=abs(vy0*vz1-vz0*vy1)
            yvec=abs(vz0*vx1-vx0*vz1)
            zvec=abs(vx0*vy1-vy0*vx1)

            longloc=pow(pow(xvec,2)+pow(yvec,2)+pow(zvec,2),0.5)

            if longloc>0.0: # las barras son paralelas si longloc=0
                
                xvec*=1.0/longloc
                yvec*=1.0/longloc
                zvec*=1.0/longloc

                vec_prod.append([xvec, yvec, zvec])

        fact=0.0
        for i in range(1,len(vec_prod),1):
            fact+=abs(vec_prod[i][0]-vec_prod[0][0])
            fact+=abs(vec_prod[i][1]-vec_prod[0][1])
            fact+=abs(vec_prod[i][2]-vec_prod[0][2])
     
        if fact/len(bars)>error_global:
            print('->  |||||| ERROR EN LA BARRA ', bars[i][0], '|||||| , esta a axil y fuera del plano') 
            error_index=1
        else:
             print('        +  Barras a axil en un mismo plano  OK')
            
    else:
        print('        +  Barras a axil en un mismo plano  OK')

    if len(bars_tors)>0:
        
        for i in range(0,len(bars_tors),1):
            fact=0
            ind_loc=bars_tors[i]
            vx1=bars[ind_loc][6]-bars[ind_loc][12]
            vy1=bars[ind_loc][7]-bars[ind_loc][13]
            vz1=bars[ind_loc][8]-bars[ind_loc][14]

            longloc=pow(pow(vx1,2)+pow(vy1,2)+pow(vz1,2),0.5)
            vx1*=1.0/longloc
            vy1*=1.0/longloc
            vz1*=1.0/longloc

            for j in range(0,len(bars_axil)):
                ind_loc2=bars_axil[j]
                vx2=bars[ind_loc2][6]-bars[ind_loc2][12]
                vy2=bars[ind_loc2][7]-bars[ind_loc2][13]
                vz2=bars[ind_loc2][8]-bars[ind_loc2][14]

                longloc=pow(pow(vx2,2)+pow(vy2,2)+pow(vz2,2),0.5)
                vx2*=1.0/longloc
                vy2*=1.0/longloc
                vz2*=1.0/longloc

                prod=vx1*vx2+vy1*vy2+vz1*vz2
                if abs(prod)>error_global:
                    fact=1

            if fact>0:
                print('->  |||||| ERROR EN LA BARRA ', bars[ind_loc][0], '|||||| , esta a torsion y no es ortogonal al plano de axiles y rigidos')
                error_index=1
            else:
                print('        +  Barra a torsion ', bars[ind_loc][0],' ortogonal al plano de axiles y rigidos  OK')
         
    else:
        print('')
        print('        No hay barras a torsion')
            
    #       torsiones
    print('')
    print('verificando torsiones ...')
    print('')
    torsi=0
    for i in range(0,len(bars),1):
        if bars[i][2]==2 :
            torsi=1
            if (int(bars[i][11])!=0 or int(bars[i][17])!=0):
                print('->  |||||| ERROR EN LA BARRA ', bars[i][0], '|||||| , las barras con torsion no pueden terminar en ')
                print('               un nudo compartido, tienen que estar empotradas en apoyos o en rigidos')
            else:
                print('        ->  La Torsion de la barra ', bars[i][0], ' OK.')

    if torsi==0:
        print('        No hay barras a torsion')

              
    # comprobar los datos de las cargas
    print('')
    print('> Congruency verification of file: '+'cargas_'+name+'_'+surname1+'_'+surname2+'.txt')
    print('')

    #       energias
    print('verificando trabajos ...')
    print('')
    for i in range(0,len(loads),1):
        if loads[i][2]==2:
            longloc=pow(pow(loads[i][8]-loads[i][11],2)+pow(loads[i][9]-loads[i][12],2)+pow(loads[i][10]-loads[i][13],2),0.5)
            load_w=loads[i][3]*longloc
            nameadd='distribuida'
            Eloc=load_w*loads[i][14]/2.0
        else:
            load_w=loads[i][3]
            if loads[i][2]==4:
                nameadd='termica'
                el_loc=int(loads[i][7])
                if bars[el_loc-1][5]!=loads[i][3]:
                    print('->  |||||| ERROR EN LA BARRA ', el_loc, '|||||| , la carga termica del fichero barras y cargas no coincide. ' )
                    print('                   Valor en cargas= ', round(loads[i][3],3), '  vs  Valor en barras=',  round(bars[el_loc-1][5],3) )
                    error_index=1
                Eloc=0.5*abs(bars[el_loc-1][3])*abs(loads[i][14])
            else:
                nameadd='puntual'
                Eloc=load_w*loads[i][14]/2.0
                
        if abs(loads[i][15]-Eloc)/Eloc>error_global:
            print('->  |||||| ERROR EN LA CARGA ', loads[i][0], '|||||| , el trabajo, la carga y el movimiento no coinciden')
            print('                   Valor calculado= ', round(Eloc,3), '  vs  Valor en el fichero=',  round(loads[i][15],3) )
            print('')
            if nameadd=='termica':
                print('     La energia termica no concuerda con su esfuerzo axil y deformacion, puede ser debido a un fallo de calculo')
                print('     o a que la energia insertada ya esta corregida por un acoplamiento de algunas deformaciones termicas, si hay' )
                print('     varias y son complementarias, en la estructura global. El alumno debe de revisarlo de manera individual ')
                print('     según los criterios seguidos en clase. Este error no evita que se ejecute la comprobacion estructural, y es')
                print('     responsabilidad del alumno tratar las cargas termicas de manera individual y verificarlas.') 
            else:
                error_index=1
        else:
            print('        +  Trabajo de la carga '+nameadd+' ', loads[i][0], ' OK')

    print('')
    print('verificando lugar de aplicacion ...')
    print('')
    for i in range(0,len(loads),1):
        if loads[i][2]==2:
            nameadd='distribuida'
        else:
            if loads[i][2]==4:
                nameadd='termica'
            else:
                nameadd='puntual'

        
        if int(loads[i][5]*loads[i][6]+loads[i][5]*loads[i][7]+loads[i][6]*loads[i][7])!=int(0):
            print('->  |||||| ERROR EN LA CARGA ', loads[i][0], '|||||| , tiene mas de un lugar de aplicacion')
            error_index=1
        else:
            print('        +  Lugar de aplicacion de la carga '+nameadd+' ', loads[i][0], ' OK')


    print('')
    print('')
    print('> Congruency verification of file: '+'nudos_'+name+'_'+surname1+'_'+surname2+'.txt')
    print('')
    print('verificando lugar de pertenencia ...')
    print('')
    for i in range(0,len(nodes),1):    
        if int(nodes[i][2]*nodes[i][3]+nodes[i][2]*nodes[i][4]+nodes[i][3]*nodes[i][4])!=int(0):
            print('->  |||||| ERROR EN EL NUDO ', nodes[i][0], '|||||| , tiene mas de un lugar de pertenencia')
            print('              Columnas 3, 4 y 5, valores  ', nodes[i][2], nodes[i][3], nodes[i][4])
            error_index=1
        else:
            print('        +  Lugar pertenencia del nudo ', nodes[i][0], ' OK')

    print('')
    print('verificando que hay maximo 3 barras por nudo ...')
    print('')
    for i in range(0,len(connect_nudos),1):
        if len(connect_nudos[i])>5: #### HERE
            print('->  |||||| ERROR EN EL NUDO ', nodes[i][0], '|||||| , tiene mas de 3 barras')
            error_index=1
        else:
            print('        +  Numero maximo de barras en el nudo  ', nodes[i][0], ' OK')
                                                            


                                                        
print('')
print('')
if error_index==0:
    print('WARNING: No se han verificado ni las coordenadas, ni la conectividad entre los elementos. Estos ')
    print('pueden generar errores en la validacion estructural si no se han introducido bien en los ficheros.')
    print('Las verificaciones de congruencia permiten que la validacion estructural pueda ejecutarse, pero no  ')
    print('aseguran que no existan errores en esos archivos, solo que son congruentes.  ')
    print('')
    print('No hay errores de congruencia en los archivos, y se comienza con la validacion estructural ...')
    print('')
   
if error_index==1 or error_index==3  or error_index==2:
    print('################################################################################')
    print('Hay errores en los archivos, hay que corregirlos y volver a ejecutar el programa')
    print('para poder acceder a la verificacion estructural y generar el archivo entregable.')
    print('################################################################################')

else:
    error_index=0
    print('')
    print('##### VALIDACION ESTRUCTURAL #####')
    print('')
    print('')
    print('DATOS DE LA ESTRUCTURA:')
    print('')
    equilib_apoy=0.0
    supports_R=0.0
    supports_M=0.0
    for  i in range(0,len(supports),1):
        if supports[i][7]==0: # si esta a torsion no cuenta
            supports_R+=1
            if supports[i][8]==0:
                equilib_apoy+=1
        else:
            supports_M+=1

    incognitas=len(bars)+supports_R*2+supports_M*1
    ecuaciones=equilib_apoy*2+len(rigids)*3+nudos_barras*2 #quito esto para ser mas conservadores +supports_M*1
    OH=incognitas-ecuaciones
    print('Orden de Hiperestaticidad: ', OH)
    print('Num. de barras a axil: ', baxil)
    print('Num. de barras a torsion: ', btors)
   # print('Num. de barras con incremento termico: ', carga_termica)
    print('Num. de cargas puntuales y repartidas: ', carga_p)
    print('Num. de momentos torsores: ', carga_torsor)
    print('Num. de rigidos: ', len(rigids))

    if (baxil+btors+carga_p+carga_torsor+len(rigids))==0:
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('->  |||||| ERROR NO HAY ESTRUCTURA ||||||')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')

    else:    
        v_energ=[]
        ener_med=0.0
        v_area=[]
        area_med=0.0
        for i in range(0,len(bars),1):
            v_area.append(bars[i][20])
            area_med+=bars[i][20]/len(bars)
            v_energ.append(bars[i][18])
            ener_med+=bars[i][18]/len(bars)

        SDE=0.0
        SDA=0.0
        for i in range(0,len(bars),1):
            SDA+=pow(bars[i][20]-area_med,2)/len(bars)
            SDE+=pow(bars[i][18]-ener_med,2)/len(bars)

        print('Desviacion tipica SDE/Emed: ', round(pow(SDE,0.5)/ener_med,2))
        print('Desviacion tipica SDA/Amed: ', round(pow(SDA,0.5)/area_med,2))
        print('')
        score=OH*10+baxil*2+btors*6+len(rigids)*15+carga_p*5+carga_torsor*10

        print('verificando el equilibrio en los nudos ...')
        print('')
        nodo_connect_forces=[]
        for  i in range(0,len(nudos_solo),1):
            nodo_connect_forces.append([])

        if len(nudos_solo)==0:
            print('        No hay nudos solo con barras')
        
        for i in range(0,len(bars),1):
            index_node_ini=bars[i][11]
            index_node_fin=bars[i][17]

            if int(index_node_ini)!=0 and nudos_solo.count(int(index_node_ini))!=0 :
                if bars[i][2]==1:
                    Fx=bars[i][3]*(bars[i][12]-bars[i][6])/bars[i][21]
                    Fy=bars[i][3]*(bars[i][13]-bars[i][7])/bars[i][21]
                    Mt=0.0
                index_loc=nudos_solo.index(int(index_node_ini))
                nodo_connect_forces[index_loc].append([Fx, Fy, Mt, bars[i][6], bars[i][7], bars[i][0]]) # meter Fx, Fy y punto

            if int(index_node_fin)!=0 and nudos_solo.count(int(index_node_fin))!=0 :
                if bars[i][2]==1:
                    Fx=bars[i][3]*(bars[i][6]-bars[i][12])/bars[i][21]
                    Fy=bars[i][3]*(bars[i][7]-bars[i][13])/bars[i][21]
                    Mt=0.0

                index_loc=nudos_solo.index(int(index_node_fin))
                nodo_connect_forces[index_loc].append([Fx, Fy, Mt, bars[i][6], bars[i][7], bars[i][0]]) # meter Fx, Fy y punto

        for i in range(0,len(loads),1):
            index_nudo=loads[i][6]
            if int(index_nudo)!=0 and int(loads[i][2])!=4:
                carga_tot=0
                if loads[i][2]==2:

                    print('')
                    print('->  |||||| ERROR EN LA CARGA ', loads[i][0], '||||||, no puede aplicarse una carga distribuida en un nudo ')
                    print('')
                    error_index=1
                    
                if loads[i][2]==1:
                    carga_tot=abs(loads[i][3])
                    x_apply=loads[i][8]
                    y_apply=loads[i][9]
                    Mt=0.0
                    
                Fx=carga_tot*math.cos(float(loads[i][4]))
                Fy=carga_tot*math.sin(float(loads[i][4]))
                
                if loads[i][2]==3:
                    Mt=loads[i][3]
                    Fx=0.0
                    Fy=0.0
                    x_apply=loads[i][8]
                    y_apply=loads[i][9]

                index_loc=nudos_solo.index(int(index_nudo))
                nodo_connect_forces[index_loc].append([Fx, Fy, Mt, x_apply, y_apply, loads[i][0]])
                

        for  i in range(0,len(nodo_connect_forces),1):
            Fxtot=0.0
            Fytot=0.0
            abs_Fxtot=0.0
            abs_Fytot=0.0
            for  j in range(0,len(nodo_connect_forces[i]),1):
                Fxtot+=nodo_connect_forces[i][j][0]
                Fytot+=nodo_connect_forces[i][j][1]
                abs_Fxtot+=abs(nodo_connect_forces[i][j][0])
                abs_Fytot+=abs(nodo_connect_forces[i][j][1])

            if int(Fxtot)!=0:
                error_loc=abs(Fxtot/(0.5*abs_Fxtot))
            else:
                error_loc=0.0
            if error_loc<error_global:
                print('        +  Equilibrio Fx del nudo ', nodes[nudos_solo[i]-1][0], ', error de', round(100*error_loc,2), '%   OK')
            else:
                print('')
                print('->  |||||| ERROR EN EL EQUILIBRIO Fx DEL NUDO ', nodes[nudos_solo[i]-1][0], '|||||| , error de', round(100*abs(Fxtot/(0.5*abs_Fxtot)),2), '%')
                print('')
                error_index=1

            if int(Fytot)!=0:
                error_loc=abs(Fytot/(0.5*abs_Fytot))
            else:
                error_loc=0.0
            if error_loc<error_global:
                print('        +  Equilibrio Fy del nudo ', nodes[nudos_solo[i]-1][0], ', error de', round(100*error_loc,2), '%   OK')
            else:
                print('')
                print('->  |||||| ERROR EN EL EQUILIBRIO Fy DEL NUDO ', nodes[nudos_solo[i]-1][0], '|||||| , error de', round(100*abs(Fytot/(0.5*abs_Fytot)),2), '%')
                print('')
                error_index=1
                    
        print('')
        print('verificando el equilibrio en los solidos rigidos ...')
        print('')
        if len(rigids)==0:
            print('        No hay rigidos')
        # conectividad rigidos
        for i in range(0,len(bars),1):
            index_rigido_ini=bars[i][10]
            index_rigido_fin=bars[i][16]

            if int(index_rigido_ini)!=0:
                if bars[i][2]==1:
                    Fx=bars[i][3]*(bars[i][12]-bars[i][6])/bars[i][21]
                    Fy=bars[i][3]*(bars[i][13]-bars[i][7])/bars[i][21]
                    Mt=0.0
                if bars[i][2]==2:
                    Fx=0.0
                    Fy=0.0
                    Mt=-bars[i][3] # hay que coger la reaccion del apoyo que es igual a menos la de la barra
                rigido_connect_forces[int(index_rigido_ini)-1].append([Fx, Fy, Mt, bars[i][6], bars[i][7], bars[i][0]]) # meter Fx, Fy y punto

            if int(index_rigido_fin)!=0:
                if bars[i][2]==1:
                    Fx=bars[i][3]*(bars[i][6]-bars[i][12])/bars[i][21]
                    Fy=bars[i][3]*(bars[i][7]-bars[i][13])/bars[i][21]
                    Mt=0.0
                if bars[i][2]==2:
                    Fx=0
                    Fy=0
                    Mt=-bars[i][3]
                rigido_connect_forces[int(index_rigido_fin)-1].append([Fx, Fy, Mt, bars[i][12], bars[i][13], bars[i][0]]) 
                
        for i in range(0,len(supports),1):
            index_rigido=supports[i][8]
            if int(index_rigido)!=0:
                Fx=supports[i][5]
                Fy=supports[i][6]
                Mt=supports[i][7]
                rigido_connect_forces[int(index_rigido)-1].append([Fx, Fy, Mt, supports[i][2], supports[i][3], supports[i][0]]) 

        for i in range(0,len(loads),1):
            index_rigido=loads[i][5]
            if int(index_rigido)!=0 and int(loads[i][2])!=4:
                len_apply=pow( pow(loads[i][8]-loads[i][11],2)+pow(loads[i][9]-loads[i][12],2)+pow(loads[i][10]-loads[i][13],2)  ,0.5)
                carga_tot=0
                if loads[i][2]==2:
                    carga_tot=abs(loads[i][3])*len_apply
                    x_apply=(loads[i][8]+loads[i][11])/2
                    y_apply=(loads[i][9]+loads[i][12])/2
                    Mt=0.0
                if loads[i][2]==1:
                    carga_tot=abs(loads[i][3])
                    x_apply=loads[i][8]
                    y_apply=loads[i][9]
                    Mt=0.0
                    
                Fx=carga_tot*math.cos(float(loads[i][4]))
                Fy=carga_tot*math.sin(float(loads[i][4]))
                
                if loads[i][2]==3:
                    Mt=loads[i][3]
                    Fx=0.0
                    Fy=0.0
                    x_apply=loads[i][8]
                    y_apply=loads[i][9]
                
                rigido_connect_forces[int(index_rigido)-1].append([Fx, Fy, Mt, x_apply, y_apply, loads[i][0]]) 

        for  i in range(0,len(rigids),1):
            Fxtot=0.0
            Fytot=0.0
            abs_Fxtot=0.0
            abs_Fytot=0.0
            Mtot=0.0
            abs_Mtot=0.0
            xcent_rig=0.0
            ycent_rig=0.0
            for j in range(0,len(rigido_connect_forces[i]),1):
                Fxtot+=rigido_connect_forces[i][j][0]
                Fytot+=rigido_connect_forces[i][j][1]
                abs_Fxtot+=abs(rigido_connect_forces[i][j][0])
                abs_Fytot+=abs(rigido_connect_forces[i][j][1])
                ## here para quitar el error de redondeo del angulo
                if abs_Fytot!=0.0:
                    if (abs_Fxtot/abs_Fytot)<fact_round:
                        Fxtot=0
                if abs_Fxtot!=0.0:
                    if (abs_Fytot/abs_Fxtot)<fact_round:
                        Fytot=0

                xcent_rig+=rigido_connect_forces[i][j][3]/len(rigido_connect_forces[i])
                ycent_rig+=rigido_connect_forces[i][j][4]/len(rigido_connect_forces[i])
                
                Mtot+=rigido_connect_forces[i][j][2]
                abs_Mtot+=abs(rigido_connect_forces[i][j][2])

            xcent=0.0 # funciona mejor con 0
            ycent=0.0 # funciona mejor con 0
            
            for j in range(0,len(rigido_connect_forces[i]),1):
                Mtot+=rigido_connect_forces[i][j][0]*(ycent-rigido_connect_forces[i][j][4]) # Fx
                abs_Mtot+=abs(rigido_connect_forces[i][j][0]*(ycent-rigido_connect_forces[i][j][4]))
                
                Mtot+=rigido_connect_forces[i][j][1]*(rigido_connect_forces[i][j][3]-xcent) # Fy
                abs_Mtot+=abs(rigido_connect_forces[i][j][1]*(rigido_connect_forces[i][j][3]-xcent))

            if int(Fxtot)!=0:
                error_loc=abs(Fxtot/(0.5*abs_Fxtot))
            else:
                error_loc=0.0
            if error_loc<error_global:
                print('        +  Equilibrio Fx del rigido ', rigids[i][0], ', error de', round(100*error_loc,2), '%   OK')
            else:
                print('')
                print('->  |||||| ERROR EN EL EQUILIBRIO Fx DEL SOLIDO ', rigids[i][0], '|||||| , error de', round(100*abs(Fxtot/(0.5*abs_Fxtot)),2), '%')
                print('')
                error_index=1

            if int(Fytot)!=0:
                error_loc=abs(Fytot/(0.5*abs_Fytot))
            else:
                error_loc=0.0
            if error_loc<error_global:
                print('        +  Equilibrio Fy del rigido ', rigids[i][0], ', error de ', round(100*error_loc,2), '%   OK')
            else:
                print('')
                print('->  |||||| ERROR EN EL EQUILIBRIO Fy DEL SOLIDO ', rigids[i][0], '|||||| , error de', round(100*abs(Fytot/(0.5*abs_Fytot)),2), '%')
                print('')
                error_index=1

            if int(Mtot)!=0:
                error_loc=abs(Mtot/(0.5*abs_Mtot))
            else:
                error_loc=0.0
            if error_loc<error_global:
                print('        +  Equilibrio Mf del rigido ', rigids[i][0], ', error de ', round(100*error_loc,2), '%   OK')
            else:
                print('')
                print('->  |||||| ERROR EN EL EQUILIBRIO Mf DEL SOLIDO ', rigids[i][0], '|||||| , error de', round(100*abs(Mtot/(0.5*abs_Mtot)),2), '%')
                print('')
                error_index=1
            
        print('')
        print('verificando el equilibrio en los apoyos ...')
        print('')
        nsupp=0
        for i in range(0, len(supports), 1):
            if supports[i][8]==0:
                nsupp+=1
                
        if nsupp==0:
            print('        No hay apoyos fuera de los rigidos')

        for i in range(0,len(bars),1):
            index_sup_ini=bars[i][9]
            index_sup_fin=bars[i][15]

            if int(index_sup_ini)!=0:
                if bars[i][2]==1:
                    Fx=bars[i][3]*(bars[i][12]-bars[i][6])/bars[i][21]
                    Fy=bars[i][3]*(bars[i][13]-bars[i][7])/bars[i][21]
                    Mt=0.0
                if bars[i][2]==2:
                    Fx=0
                    Fy=0
                    Mt=bars[i][3]
                    
                supports_connect[int(index_sup_ini)-1].append([Fx, Fy, Mt, bars[i][6], bars[i][7], bars[i][0]]) # meter Fx, Fy y punto

            if int(index_sup_fin)!=0:
                if bars[i][2]==1:
                    Fx=bars[i][3]*(bars[i][6]-bars[i][12])/bars[i][21]
                    Fy=bars[i][3]*(bars[i][7]-bars[i][13])/bars[i][21]
                    Mt=0.0
                if bars[i][2]==2:
                    Fx=0
                    Fy=0
                    Mt=bars[i][3]
                    
                supports_connect[int(index_sup_fin)-1].append([Fx, Fy, Mt, bars[i][12], bars[i][13], bars[i][0]])

        for  i in range(0,len(supports),1):
            if supports[i][8]==0:
                Fx=supports[i][5]
                abs_Fx=abs(supports[i][5])
                Fy=supports[i][6]
                abs_Fy=abs(supports[i][6])
                Mt=supports[i][7]
                abs_Mt=abs(supports[i][7])
                
                for j in range(0,len(supports_connect[i]),1):
                    Fx+=supports_connect[i][j][0]
                    abs_Fx+=abs(supports_connect[i][j][0])
                    Fy+=supports_connect[i][j][1]
                    abs_Fy+=abs(supports_connect[i][j][1])
                    Mt+=supports_connect[i][j][2]
                    abs_Mt+=abs(supports_connect[i][j][2])

                if int(Fx)!=0:
                    error_loc=abs(Fx/(0.5*abs_Fx))
                else:
                    error_loc=0.0
                    
                if error_loc<error_global:
                    print('        +  Equilibrio Fx del apoyo ', supports[i][0], ', error de ', round(100.0*error_loc,2), '%   OK')
                else:
                    print('')
                    print('->  |||||| ERROR EN EL EQUILIBRIO Fx DEL APOYO ', supports[i][0], '|||||| , error de', round(100*abs(Fx/(0.5*abs_Fx)),2), '%')
                    print('')
                    error_index=1

                if int(Fy)!=0:
                    error_loc=abs(Fy/(0.5*abs_Fy))
                else:
                    error_loc=0.0
                    
                if error_loc<error_global:
                    print('        +  Equilibrio Fy del apoyo ', supports[i][0], ', error de ', round(100.0*error_loc,2), '%   OK')
                else:
                    print('')
                    print('->  |||||| ERROR EN EL EQUILIBRIO Fy DEL APOYO ', supports[i][0], '|||||| , error de', round(100*abs(Fy/(0.5*abs_Fy)),2), '%')
                    print('')
                    error_index=1
                    
                if int(Mt)!=0:
                    error_loc=abs(Mt/(0.5*abs_Mt))
                else:
                    error_loc=0.0
                    
                if error_loc<error_global:
                    print('        +  Equilibrio Mf del apoyo ', supports[i][0], ', error de ', round(100.0*error_loc,2), '%   OK')
                else:
                    print('')
                    print('->  |||||| ERROR EN EL EQUILIBRIO Mf DEL APOYO ', supports[i][0], '|||||| , error de', round(100*abs(Mt/(0.5*abs_Mt)),2), '%')
                    print('')
                    error_index=1

        print('')
        print('verificando el equilibrio global ...')
        print('')
        Fxglob=0.0
        Fyglob=0.0
        Mtglob=0.0
        abs_Fxglob=0.0
        abs_Fyglob=0.0
        abs_Mtglob=0.0
        xcentre=0.0
        ycentre=0.0
        xmid=0.0
        ymid=0.0
        for i in range(0,len(supports),1): # sumatorio reacciones
            Fxglob+=supports[i][5]
            Fyglob+=supports[i][6]
            abs_Fxglob+=abs(supports[i][5])
            abs_Fyglob+=abs(supports[i][6])
            Mtglob+=supports[i][7]
            abs_Mtglob+=abs(supports[i][7])
            Mtglob+=supports[i][5]*(ycentre-supports[i][3])
            abs_Mtglob+=abs(supports[i][5]*(ycentre-supports[i][3]))
            Mtglob+=supports[i][6]*(supports[i][2]-xcentre)
            abs_Mtglob+=abs(supports[i][6]*(supports[i][2]-xcentre))
            xmid+=supports[i][2]/len(supports)
            ymid+=supports[i][3]/len(supports)

        for i in range(0,len(loads),1):
            if int(loads[i][2])!=4: # la carga no es termica
                len_apply=pow( pow(loads[i][8]-loads[i][11],2)+pow(loads[i][9]-loads[i][12],2)+pow(loads[i][10]-loads[i][13],2)  ,0.5)
                carga_tot=0.0
                if loads[i][2]==2:
                    carga_tot=abs(loads[i][3])*len_apply
                    x_apply=(loads[i][8]+loads[i][11])/2.0
                    y_apply=(loads[i][9]+loads[i][12])/2.0
                    Mt=0.0
                if loads[i][2]==1:
                    carga_tot=abs(loads[i][3])
                    x_apply=float(loads[i][8])
                    y_apply=float(loads[i][9])
                    Mt=0.0
                    
                Fx=carga_tot*math.cos(float(loads[i][4]))
                Fy=carga_tot*math.sin(float(loads[i][4]))
                
                if loads[i][2]==3:
                    Mt=loads[i][3]
                    Fx=0.0
                    Fy=0.0
                    x_apply=loads[i][8]
                    y_apply=loads[i][9]

                Fxglob+=Fx
                Fyglob+=Fy
                abs_Fxglob+=abs(Fx) #
                abs_Fyglob+=abs(Fy) #
                Mtglob+=Mt
                Mtglob+=Fx*(ycentre-y_apply)
                Mtglob+=Fy*(x_apply-xcentre)
                abs_Mtglob+=abs(Mt) #
                abs_Mtglob+=abs(Fx*(ycentre-y_apply)) #
                abs_Mtglob+=abs(Fy*(x_apply-xcentre)) #

        ## here para quitar el error de redondeo del angulo
        if abs_Fyglob!=0.0:
            if (abs_Fxglob/abs_Fyglob)<fact_round:
                Fxglob=0
                
        if abs_Fxglob!=0.0:
            if (abs_Fyglob/abs_Fxglob)<fact_round:
                Fyglob=0
                        
        if int(Fxglob)!=0:
            error_loc=abs(Fxglob/(0.5*abs_Fxglob))
        else:
            error_loc=0.0
            
        if error_loc<error_global:
            print('        +  Equilibrio Fx global, error de ', round(100.0*error_loc,2), '%   OK')
        else:
            print('')
            print('->  |||||| ERROR EN EL EQUILIBRIO Fx GLOBAL |||||| , error de', abs_Fxglob,abs_Fyglob, round(100*abs(Fxglob/(0.5*abs_Fxglob)),2), '%')
            print('')
            error_index=1

        if int(Fyglob)!=0:
            error_loc=abs(Fyglob/(0.5*abs_Fyglob))
        else:
            error_loc=0.0
            
        if error_loc<error_global:
            print('        +  Equilibrio Fy global, error de ', round(100.0*error_loc,2), '%   OK')
        else:
            print('')
            print('->  |||||| ERROR EN EL EQUILIBRIO Fy GLOBAL |||||| , error de', round(100*abs(Fyglob/(0.5*abs_Fyglob)),2), '%')
            print('')
            error_index=1
            
        if int(Mtglob)!=0:
            error_loc=abs(Mtglob/(0.5*abs_Mtglob))
        else:
            error_loc=0.0
            
        if error_loc<error_global:
            print('        +  Equilibrio Mf global, error de ', round(100.0*error_loc,2), '%   OK')
        else:
            print('')
            print('->  |||||| ERROR EN EL EQUILIBRIO Mf GLOBAL |||||| , error de', round(100*abs(Mtglob/(0.5*abs_Mtglob)),2), '%')
            print('')
            error_index=1
        
        print('')
        print('verificando el equilibrio de energias ...')
        print('')

        energ_externa=0.0
        for i in range(0,len(loads),1):
            energ_externa+=loads[i][15]
        
        energ_int=0.0
        for i in range(0,len(bars),1):
            energ_int+=bars[i][18]

        if int(energ_externa)!=0:
            error_loc=abs((energ_externa-energ_int)/(energ_externa))
        else:
            error_loc=10000000.0
            
        if error_loc<error_global:
            print('        +  Equilibrio energetico global, error de ', round(100.0*error_loc,2), '%   OK')
        else:
            print('')
            print('->  |||||| ERROR EN EL EQUILIBRIO ENERGETICO GLOBAL |||||| , error de', round(100.0*error_loc,2), '%')
            print('')
            error_index=1

        if error_index==1:
            print('')
            print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
            print('')
            print('           Existen errores estructurales, hay que corregirlos y volver a ejecutar el programa.')
            print('')
            print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
            print('')
            print('')
            print('     Hay que ver los errores y los elementos implicados, los fallos pueden estar producidos tanto por datos')
            print('     mal introducidos en los ficheros como por fallos de calculo estructural')
            print('')
            print('')
        else:
            print('')
            print('')
            print('--------------------------------------------------------------------------------------------------------')
            print('##### ESTRUCTURA VALIDADA ####################################')
            print('')
            print( name, surname1, surname2)
            print('')
            print('                              PUNTUACION DE LA ESTRUCTURA (PE): ', int(score))
            print('                              DESVIACION TIPICA NORMALIZADA (SDW): ', round(pow(SDE,0.5)/ener_med+pow(SDA,0.5)/area_med,5))
            print('')
            print('#########################################################')
            print('--------------------------------------------------------------------------------------------------------')
            print('')
            print('')

            ### print in a file the results

            fcert=open('validated_structure_'+name+'_'+ surname1+'_'+surname2+'.txt', 'w')
            fcert.write('\n')
            fcert.write('\n')
            fcert.write('-------------------------------------------------------------------')
            fcert.write('\n')
            fcert.write('           ##### ESTRUCTURA VALIDADA #####')
            fcert.write('\n')
            fcert.write('-------------------------------------------------------------------')
            fcert.write('\n')
            fcert.write('\n')
            fcert.write('  '+ name+' '+ surname1+' '+ surname2)
            fcert.write('\n')
            fcert.write('\n')
            fcert.write('  '+str(DNI_num)+ '-'+DNI_letra+'   '+grupo)
            fcert.write('\n')
            fcert.write('  '+mail)
            fcert.write('\n')
            fcert.write('\n')
            fcert.write('-------------------------------------------------------------------')
            fcert.write('\n')
            fcert.write('\n')
            fcert.write('  Orden de Hiperestaticidad: '+ str(OH))
            fcert.write('\n')
            fcert.write('  Num. de barras a axil: '+ str(baxil))
            fcert.write('\n')
            fcert.write('  Num. de barras a torsion: '+ str(btors))
            fcert.write('\n')
            fcert.write('  Num. de barras con incremento termico: '+ str(carga_termica))
            fcert.write('\n')
            fcert.write('  Num. de cargas puntuales y repartidas: '+ str(carga_p))
            fcert.write('\n')
            fcert.write('  Num. de momentos torsores: '+ str(carga_torsor))
            fcert.write('\n')
            fcert.write('  Num. de rigidos: '+str( len(rigids)))
            fcert.write('\n')
            fcert.write('  Desviacion tipica SDE/Emed: '+ str(round(pow(SDE,0.5)/ener_med,2)))
            fcert.write('\n')
            fcert.write('  Desviacion tipica SDA/Amed: '+ str(round(pow(SDA,0.5)/area_med,2)))
            fcert.write('\n')
            fcert.write('\n')
            fcert.write('-------------------------------------------------------------------')
            fcert.write('\n')
            fcert.write('\n')
            fcert.write('        PUNTUACION DE LA ESTRUCTURA (PE): '+str( int(score)))
            fcert.write('\n')
            fcert.write('        DESVIACION TIPICA NORMALIZADA (SDW): '+str(round(pow(SDE,0.5)/ener_med+pow(SDA,0.5)/area_med,5)))
            fcert.write('\n')
            fcert.write('\n')
            fcert.write('-------------------------------------------------------------------')
            fcert.write('\n')
            fcert.write('\n')
         
            fcert.close()

            fcell= open('datos_personales.txt','r')
            fw2=open('datos_personales_'+name+'_'+surname1+'_'+surname2+'.txt','w')
            for line in fcell.readlines() :
                vecaux=[str(x) for x in line.split()]
                for k in range(0,len(vecaux),1):
                    fw2.write(vecaux[k])
                    fw2.write('  ')
                fw2.write('\n')

            fcell.close()
            fw2.close()








