import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_services import analyse_credit_card

def show_image_and_validation(blob_url, credit_card_info):
    # st.write("Informações de cartão de crédito encontradas:")
    # st.write(credit_card_info)

    st.image(blob_url, caption = "Imagem eviada", use_container_width=True)
    st.write("Resultado da validação:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green';>Cartão Válido</1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular: {credit_card_info['card_name']}")
        st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
        st.write(f"Data de Validade: {credit_card_info['expiry_date']}")
    else:
        st.markdown(f"<h1 style='color: red';>Cartão Inválido</1>", unsafe_allow_html=True)
        st.write("O arquivo enviado não condiz com um cartão de crédito")
    
def configure_interface():
    st.title("Upload de Arquivo DIO - Desafio 1 - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        # Enviar para o blob storage do azure
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url is not None:
            st.write(f"Arquivo {fileName} enviado com sucesso para o Azure Blob Storage")
            credit_card_info = analyse_credit_card(blob_url) # Chamar a função de detecção de informações de cartão de crédito
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo {fileName} para o Azure Blob Storage!")

if __name__ == '__main__':
    configure_interface()