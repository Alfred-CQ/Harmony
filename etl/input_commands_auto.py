import subprocess

#copyFromLocal,cp,copyToLocal
def execute_comando_hadoop(tipe_consult,archiv,destination):
    if tipe_consult not in ['copyFromLocal', 'cp' , 'copyToLocal' ]:
        print("Tipo de consulta no válido. Debe ser 'copyFromLocal', 'cp','copyToLocal', etc.")
        return

    comando_hadoop = f"hdfs dfs -{tipe_consult} {archiv} {destination}"

    print(f"La salida del comando: {comando_hadoop}")

    try:
        resultado = subprocess.run(comando_hadoop, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if resultado.returncode == 0:
            print("Ejecución del comando exitosa:")
            print(resultado.stdout)
        else:
            print("Error al ejecutar el comando:")
            print(resultado.stderr)
    except Exception as e:
        print(f"Error: {str(e)}")

#streaming
def execute_comando_hadoop2(input1,input2,input3,input4,input5):
    
    comando_hadoop_t = f"hadoop-streaming -D -mapred.reduce.tasks={input1} \-file {input2} -mapper {input2} \-file {input3} -reducer {input3} \-input {input4} -output {input5}"

    print(f"La salida del comando: {comando_hadoop_t}")

    try:
        resultado = subprocess.run(comando_hadoop_t, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if resultado.returncode == 0:
            print("Ejecución del comando exitosa:")
            print(resultado.stdout)
        else:
            print("Error al ejecutar el comando:")
            print(resultado.stderr)
    except Exception as e:
        print(f"Error: {str(e)}")

#ejecutar_comando_hadoop2(1,"/home/hadoop/Harmony/samples/inverted_index/mapper.py","/home/hadoop/Harmony/samples/inverted_index/reducer.py","/user/hadoop/input","/user/hadoop/output")
