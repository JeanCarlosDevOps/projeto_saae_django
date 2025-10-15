# Dentro do arquivo avisos/models.py

from django.db import models

class Bairro(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do Bairro")

    def __str__(self):
        return self.nome

class AvisoFaltaDagua(models.Model):
    STATUS_CHOICES = [
        ('RASCUNHO', 'Rascunho'),
        ('ENVIADO', 'Enviado para Processamento'),
        ('CONCLUIDO', 'Concluído'),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título do Aviso")
    mensagem = models.TextField(verbose_name="Mensagem Completa")
    data_inicio_previsto = models.DateTimeField(verbose_name="Data e Hora de Início Previsto")
    data_fim_previsto = models.DateTimeField(verbose_name="Data e Hora de Fim Previsto")
    bairros_afetados = models.ManyToManyField(Bairro, verbose_name="Bairros Afetados")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='RASCUNHO')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_envio = models.DateTimeField(null=True, blank=True, verbose_name="Data do Envio")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Aviso de Falta D'água"
        verbose_name_plural = "Avisos de Falta D'água"