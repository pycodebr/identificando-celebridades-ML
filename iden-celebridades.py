import boto3
import json

def recognize_celebrities(photo):

    # Cria o serviço com as suas credenciais da AWS #
    client=boto3.client(
        service_name='rekognition',
        region_name='us-east-1',
        aws_access_key_id='***SUA ACCESS_KEY***', 
        aws_secret_access_key='***SUA SECRET_KEY***'      
    )

    # Envia imagem para analise no serviço AWS Rekognition e captura resultados #
    with open(photo, 'rb') as image:
        response = client.recognize_celebrities(Image={'Bytes': image.read()})

    # Mostra resultados obtidos #
    for celebrity in response['CelebrityFaces']:
        print ('\n Nome: ' + celebrity['Name'])
        print (' Id: ' + celebrity['Id'])
        print (' Posição:')
        print ('   Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
        print ('   Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
        print (' Info')
        for url in celebrity['Urls']:
            print ('   ' + url)
        print
    return len(response['CelebrityFaces'])

def main():
    photo = input("Digite o local onde está a imagem: ")

    celeb_count=recognize_celebrities(photo)
    print("\n Celebridades detectadas: " + str(celeb_count))

if __name__ == "__main__":
    main()