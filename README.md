# Sistema de Gerenciamento de Alunos e Cursos

Este projeto foi desenvolvido como parte da disciplina de Back-End para o curso do CESMAC. O objetivo é criar um sistema de gerenciamento de alunos e cursos utilizando o framework Django.

## 🎯 Objetivo

Desenvolver um sistema básico para uma empresa do setor educacional que está começando suas atividades e necessita de um sistema para manter e organizar os dados de seus alunos e cursos.

### Requisitos da Experiência de Aprendizagem

A atividade está dividida em quatro passos, que devem ser implementados para concluir a experiência.

### 📝 Passos

1. **Passo 1**:
   - Criar o modelo `Aluno` com os campos:
     - `nome`
     - `sobrenome`
     - `email`

2. **Passo 2**:
   - Criar o modelo `Curso` com os campos:
     - `titulo`
     - `descricao`
   - Relacionamento: Um aluno pode estar matriculado em vários cursos.

3. **Passo 3**:
   - Configurar o Django Admin para cadastrar alunos.
   - Criar uma URL e uma view para exibir os alunos cadastrados.
   - Criar templates para exibir a lista de alunos.

4. **Passo 4**:
   - Configurar o Django Admin para cadastrar cursos.
   - Criar uma URL e uma view para exibir os cursos cadastrados.
   - Criar templates para exibir a lista de cursos.

---

## ⚙️ Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/hywenklis/educational-system.git
   cd educational-system
   ```

2. Crie um ambiente virtual (opcional):
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Para Linux/macOS
   venv\Scripts\activate      # Para Windows
   ```
   
3. Execute as migrações para criar o banco de dados:
   ```bash
   python manage.py migrate
   ```

4. Crie um superusuário para acessar o Django Admin (opcional):
   ```bash
   python manage.py createsuperuser
   ```

5. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```
---

## 🌐 URLs e Views

- `/school/students`: Exibe a lista de alunos cadastrados.
- `/school/courses`: Exibe a lista de cursos cadastrados.

## 📸 Capturas de Tela
![image](https://github.com/user-attachments/assets/26e44cf6-4996-4074-8fe0-e3c64088d623)
![image](https://github.com/user-attachments/assets/eb4c4750-d52a-428f-80fd-deb84c260793)


---

## 🔄 Como Contribuir

Este projeto faz parte de uma experiência de aprendizagem, mas sinta-se à vontade para sugerir melhorias ou corrigir problemas.

---

Com este README, você pode fornecer uma descrição completa do projeto, facilitando a avaliação e apresentando a implementação e as telas com as capturas de tela solicitadas.
