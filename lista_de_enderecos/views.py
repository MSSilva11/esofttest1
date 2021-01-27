from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from django.template.defaultfilters import linebreaksbr

from lista_de_enderecos.models import Dados

class EnderecoForm(ModelForm):
    class Meta:
        model = Dados
        fields = ['cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'uf', 'descricao']

def endereco_list(request, template_name='endereco_list.html'):
    endereco = Dados.objects.all()
    data = {'lista': endereco}

    return render(request, template_name, data)

def endereco_cadastro(request, template_name='form_endereco.html'):
    form = EnderecoForm(request.POST or None)

    endereco = Dados.objects.all()

    if request.method == 'POST':
        if form.is_valid():
            end_cep = form.cleaned_data['cep']

            Teste = Dados.objects.filter(cep=end_cep)

            if not Teste:
                end_endereco = form.cleaned_data['endereco']
                end_numero = form.cleaned_data['numero']
                end_complemento = form.cleaned_data['complemento']
                end_bairro = form.cleaned_data['bairro']
                end_cidade = form.cleaned_data['cidade']
                end_uf = form.cleaned_data['uf']
                end_descricao = form.cleaned_data['descricao']

                new = Dados(cep=end_cep, endereco=end_endereco, numero=end_numero, complemento=end_complemento,
                                bairro=end_bairro, cidade=end_cidade, uf=end_uf, descricao=end_descricao)

                new.save()

            else:
                pk = Dados.objects.get(cep=end_cep)
                form = EnderecoForm(request.POST, instance=pk)

                edit = form.save(commit=False)
                edit.cep = form.cleaned_data['cep']
                edit.endereco = form.cleaned_data['endereco']
                edit.numero = form.cleaned_data['numero']
                edit.complemento = form.cleaned_data['complemento']
                edit.bairro = form.cleaned_data['bairro']
                edit.cidade = form.cleaned_data['cidade']
                edit.uf = form.cleaned_data['uf']
                edit.descricao = form.cleaned_data['descricao']

                edit.save()

            return redirect('dados_list')

    return render(request, template_name, {'form': form, 'lista': endereco})

def endereco_excluir(request, template_name='endereco_excluir.html'):
    id = request.GET.get('id')
    endereco = Dados.objects.filter(id=id)
    data = {'selecionado': endereco}

    if request.method == 'POST':
        Dados.objects.filter(id=id).delete()
        return redirect('dados_list')

    return render(request, template_name, data)