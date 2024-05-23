def email_confirm(protocol: str, base_url: str) -> str:
    return f"""
        <html>
        <body style="padding: 0; margin: 0;">
            <div style="text-align: center; width: 100%">
                <h1 style="margin-bottom: 4rem;">Confirmação de E-mail: Publisher</h1>
                <a
                    href="{base_url}/v1/confirm_account/{protocol}"
                    style="
                        padding: 1rem 2rem;
                        background: #3cb371;
                        color: #fff;
                        border-radius: .5rem;
                        text-decoration: none;">Confirmar E-mail</a>
                <p style="margin-top: 4rem;">
                    Esse é o link para confirmação da sua conta na plataforma
                    Publisher. Acesse e será redirecionado para a página de login
                    do serviço.
                </p>
            </div>
        </body>
        </html>
    """
