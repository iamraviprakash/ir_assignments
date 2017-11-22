import os

def remove_non_ascii(filepath):

    for folder,subfolders,files in os.walk(filepath):

        for filename in files:

            ip=open((os.path.join(os.path.abspath(folder),filename)),'r')
            final_text=''
            for line in ip:
                line=line.strip().decode("ascii","ignore").encode("ascii")
                if line=="":
                    continue
                final_text+=line+' '
            ip.close()

            op=open((os.path.join(os.path.abspath(folder),filename)),'w')
            op.write(final_text)
            op.close()
