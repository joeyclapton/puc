# Atividade 01 - Requisitos não funcionais Mentcare, Sommerville

## Requisitos não funcionais - Segurança

- O sistema deve permitir o armazenamento dos logs de auditoria fora do servidor de banco de dados principal.
- O sistema deve bloquear captura de tela em smartphones.
- O sistema deve implementar ferramentas e soluções contra vazamento de dados, como DLP(data loss prevention)
- Os dados inseridos no sistema deverão ser salvos usando criptografia AES 256 bits
- O login no sistema deverá ser por meio de controle de acesso
- Ocultar dados não importantes baseados na lista de acesso
- O sistema deve gerar tokens de acesso que se expiram a cada X tempo
- O sistema deverá prover backup dos dados
- O sistema deve fazer uso de HTTPS em todas as páginas de navegação
- O sistema deve prover um canal de autenticação segura com 1 ou mais fatores de segurança(como email, sms, tokens...)

### Referências

(Software Engineering. Ian Sommerville. Mentcare: A mental health support system)[https://software-engineering-book.com/case-studies/mentcare/]
