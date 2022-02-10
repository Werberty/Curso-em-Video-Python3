larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg*alt
print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m²')
print(f'Para pintar essa parede, você precisará de {0.5*area}L de tinta')
