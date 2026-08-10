# CAMINHO COMPLETO: C:\Users\vlula\OneDrive\Área de Trabalho\Projetos Backup\NETTSAN_PORTAL\criar_estrutura_nettsan_portal.ps1
# DATA E HORA DO ULTIMO RECODE: 2026-08-10 10:40 -03:00
# MOTIVO DA ALTERACAO: Criar somente a estrutura inicial de pastas do projeto NETTSAN_PORTAL, sem criar codigo da aplicacao.

$ErrorActionPreference = "Stop"

$RaizProjetos = "C:\Users\vlula\OneDrive\Área de Trabalho\Projetos Backup"
$Projeto = Join-Path $RaizProjetos "NETTSAN_PORTAL"

$Pastas = @(
    $Projeto,
    (Join-Path $Projeto "templates"),
    (Join-Path $Projeto "static"),
    (Join-Path $Projeto "static\css"),
    (Join-Path $Projeto "static\js"),
    (Join-Path $Projeto "static\img"),
    (Join-Path $Projeto "static\img\brand"),
    (Join-Path $Projeto "static\img\home"),
    (Join-Path $Projeto "static\img\gestflow"),
    (Join-Path $Projeto "static\img\indflow"),
    (Join-Path $Projeto "static\img\nr12"),
    (Join-Path $Projeto "static\img\cases"),
    (Join-Path $Projeto "docs")
)

foreach ($Pasta in $Pastas) {
    if (-not (Test-Path $Pasta)) {
        New-Item -ItemType Directory -Path $Pasta | Out-Null
        Write-Host "CRIADA: $Pasta"
    }
    else {
        Write-Host "JA EXISTE: $Pasta"
    }
}

Write-Host ""
Write-Host "Estrutura inicial do NETTSAN_PORTAL criada com sucesso."
Write-Host "Nenhum arquivo da aplicacao foi criado ou alterado."
