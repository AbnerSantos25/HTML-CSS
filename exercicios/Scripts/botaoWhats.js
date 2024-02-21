// Criação da tag link para carregar o Font Awesome
var link = document.createElement("link");
link.rel = "stylesheet";
link.href = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css";
// Adiciona a tag link ao head do documento
document.head.appendChild(link);

// Função para adicionar o botão flutuante do WhatsApp dinamicamente
function adicionarBotaoWhatsApp() {
    var numeroTelefone = "17997556141"; // Seu número de telefone

    // Criação do elemento do botão
    var whatsappButton = document.createElement("a");
    whatsappButton.href = "https://wa.me/" + numeroTelefone;
    whatsappButton.target = "_blank";
    whatsappButton.classList.add("whatsapp-btn");
    whatsappButton.innerHTML = '<i class="fab fa-whatsapp"></i>';

    // Estilos do botão
    whatsappButton.style.position = "fixed";
    whatsappButton.style.bottom = "20px";
    whatsappButton.style.right = "20px";
    whatsappButton.style.zIndex = "9999";
    whatsappButton.style.backgroundColor = "#25d366";
    whatsappButton.style.color = "#fff";
    whatsappButton.style.padding = "15px 25px";
    whatsappButton.style.borderRadius = "50%";
    whatsappButton.style.fontSize = "80px";
    whatsappButton.style.boxShadow = "0px 0px 20px rgba(0, 0, 0, 0.1)";
    whatsappButton.style.transition = "all 0.3s ease";

    // Estilos de hover do botão
    whatsappButton.addEventListener("mouseenter", function() {
    whatsappButton.style.backgroundColor = "#128c7e";
    });

    whatsappButton.addEventListener("mouseleave", function() {
    whatsappButton.style.backgroundColor = "#25d366";
    });

    // Adiciona o botão ao corpo do documento
    document.body.appendChild(whatsappButton);
}

// Chama a função para adicionar o botão do WhatsApp
adicionarBotaoWhatsApp();
        
