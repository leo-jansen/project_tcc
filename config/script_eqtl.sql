-- Criar o novo banco de dados Equatorial
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'Equatorial')
BEGIN
    CREATE DATABASE Equatorial;
END;
GO

-- Conectar ao banco de dados Equatorial
USE Equatorial;
GO

-- Criação do esquema Control
IF NOT EXISTS (SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'Control')
BEGIN
    EXEC('CREATE SCHEMA Control;');
END;
GO

-- Criar a tabela Company dentro do esquema Control
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[Control].[Company]') AND type in (N'U'))
BEGIN
    CREATE TABLE [Control].[Company](
        [id_company] [int] IDENTITY(1,1) NOT NULL,
        [nm_company] [nvarchar](100) NOT NULL,
        [status] [char](1) NOT NULL DEFAULT 'N' CHECK ([status] IN ('S', 'N')),
        CONSTRAINT [Company_PK] PRIMARY KEY CLUSTERED ([id_company] ASC)
    );
END;
GO

-- Criar a tabela Profile dentro do esquema Control
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[Control].[Profile]') AND type in (N'U'))
BEGIN
    CREATE TABLE [Control].[Profile](
        [profile_id] [int] IDENTITY(1,1) NOT NULL,
        [profile_nm] [nvarchar](100) NULL,
        [status] [char](1) NULL DEFAULT 'N' CHECK ([status] IN ('S', 'N')),
        [Obs] [nvarchar](max) NULL,
        CONSTRAINT [Profile_PK] PRIMARY KEY CLUSTERED ([profile_id] ASC)
    );
END;
GO


-- Criação da tabela UsrData dentro do esquema Control
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[Control].[UsrData]') AND type in (N'U'))
BEGIN
    CREATE TABLE [Control].[UsrData](
        [usr_id] [int] IDENTITY(1,1) NOT NULL,
        [usr_nm] [nvarchar](200) NULL,
        [usr_pwd] [nvarchar](max) NULL,
        [profile_id] [int] NULL,
        [id_company] [int] NULL,
        [usr_login] [nvarchar](200) NULL,
        [usr_email] [nvarchar](200) NULL,
        [usr_status] [char](1) NULL,
        [last_login] [datetime] NULL,
        [last_page] [nvarchar](max) NULL,
        CONSTRAINT [UsrData_PK] PRIMARY KEY CLUSTERED ([usr_id] ASC)
    );
END;
GO

-- Inserção de dados na tabela Company
INSERT INTO [Control].[Company] ([nm_company], [status]) VALUES (N'GERAL', N'S');
INSERT INTO [Control].[Company] ([nm_company], [status]) VALUES (N'Empresa A', N'S');
INSERT INTO [Control].[Company] ([nm_company], [status]) VALUES (N'Empresa B', N'N');
INSERT INTO [Control].[Company] ([nm_company], [status]) VALUES (N'Empresa C', N'S');
INSERT INTO [Control].[Company] ([nm_company], [status]) VALUES (N'Empresa D', N'N');

-- Inserção de dados na tabela Profile
INSERT INTO [Control].[Profile] ([profile_nm], [status], [Obs]) VALUES (N'Admin Geral', N'S', N'Admin Geral do Sistema, pode Cadastrar usuários em qualquer empresa e cadastrar/editar Empresas');
INSERT INTO [Control].[Profile] ([profile_nm], [status], [Obs]) VALUES (N'Admin Empresa', N'S', N'Adim de uma empresa, só pode cadastrar usuários na própria empresa');
INSERT INTO [Control].[Profile] ([profile_nm], [status], [Obs]) VALUES (N'Empresa', N'S', N'Usuário da empresa');

-- Inserção de dados na tabela UsrData
INSERT INTO [Control].[UsrData] ([usr_nm], [usr_pwd], [profile_id], [id_company], [usr_login], [usr_email], [usr_status])
VALUES (N'Gabriel Alboretti', N'$2b$12$hi0gE3DUQhDXMAf45fP9meysP5v9C3MWKwYLhL4UtC.avHsiU1TJe', 2, 2, N'gabriel.alboretti', N'gabriel.alboretti@empresaA.com.br', N'S');

INSERT INTO [Control].[UsrData] ([usr_nm], [usr_pwd], [profile_id], [id_company], [usr_login], [usr_email], [usr_status])
VALUES (N'Leonardo Fontes', N'$2b$12$hi0gE3DUQhDXMAf45fP9meysP5v9C3MWKwYLhL4UtC.avHsiU1TJe', 3, 2, N'leonardo.fontes', N'leonardo.fontes@empresaA.com.br', N'S');

INSERT INTO [Control].[UsrData] ([usr_nm], [usr_pwd], [profile_id], [id_company], [usr_login], [usr_email], [usr_status])
VALUES (N'Rodrigo Nascimento', N'$2b$12$hi0gE3DUQhDXMAf45fP9meysP5v9C3MWKwYLhL4UtC.avHsiU1TJe', 1, 1, N'rodrigo.nascimento', N'rodrigo.nascimento@geral.com.br', N'S');

INSERT INTO [Control].[UsrData] ([usr_nm], [usr_pwd], [profile_id], [id_company], [usr_login], [usr_email], [usr_status])
VALUES (N'Daniel Carolindo', N'$2b$12$hi0gE3DUQhDXMAf45fP9meysP5v9C3MWKwYLhL4UtC.avHsiU1TJe', 3, 4, N'daniel.carolindo', N'daniel.carolindo@empresaC.com.br', N'S');

-- Adicionando restrições de chave estrangeira
ALTER TABLE [Control].[UsrData] WITH CHECK ADD CONSTRAINT [UsrData_FK] FOREIGN KEY([id_company]) REFERENCES [Control].[Company] ([id_company]);
ALTER TABLE [Control].[UsrData] CHECK CONSTRAINT [UsrData_FK];

ALTER TABLE [Control].[UsrData] WITH CHECK ADD CONSTRAINT [UsrData_FK2] FOREIGN KEY([profile_id]) REFERENCES [Control].[Profile] ([profile_id]);
ALTER TABLE [Control].[UsrData] CHECK CONSTRAINT [UsrData_FK2];
