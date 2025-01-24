################################################################

muestra = pd.read_csv("muestra_calidad_vida.csv")

Y = muestra['esp_vida']
X = muestra[['habitantes','ingresos','analfabetismo', 'asesinatos','universitarios','heladas','area','densidad_pobl']]

# Agregar una constante para el término de intersección
X = sm.add_constant(X)

# Ajustar el modelo de regresión lineal
modelo = sm.OLS(Y, X).fit()

################################################################