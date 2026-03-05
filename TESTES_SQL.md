# TESTES SQL - VALIDAÇÃO DE PERSISTÊNCIA

Este arquivo contém queries SQL para validar a persistência dos dados e testar os relacionamentos entre as tabelas usando JOINs.

## 1. Consultar Veículos com Marca e Modelo (INNER JOIN)

```sql
SELECT 
    v.id,
    v.descricao AS veiculo,
    ma.nome AS marca,
    mo.nome AS modelo,
    v.ano,
    v.horimetro
FROM api_telemetria_veiculo v
INNER JOIN api_telemetria_marca ma ON v.marca_id = ma.id
INNER JOIN api_telemetria_modelo mo ON v.modelo_id = mo.id
ORDER BY v.id;
```

**Objetivo:** Validar relacionamento entre Veiculo, Marca e Modelo.

---

## 2. Consultar Medições com Unidade de Medida (INNER JOIN)

```sql
SELECT 
    med.id,
    med.tipo AS tipo_medicao,
    um.nome AS unidade_medida
FROM api_telemetria_medicao med
INNER JOIN api_telemetria_unidademedida um ON med.unidade_medida_id = um.id
ORDER BY med.id;
```

**Objetivo:** Validar relacionamento entre Medicao e UnidadeMedida.

---

## 3. Consultar Todas as Medições de Veículos com Relacionamentos Completos (MÚLTIPLOS JOINS)

```sql
SELECT 
    mv.id,
    v.descricao AS veiculo,
    ma.nome AS marca,
    mo.nome AS modelo,
    v.ano,
    med.tipo AS tipo_medicao,
    um.nome AS unidade_medida,
    mv.valor,
    mv.data AS data_medicao
FROM api_telemetria_medicaoveiculo mv
INNER JOIN api_telemetria_veiculo v ON mv.veiculo_id = v.id
INNER JOIN api_telemetria_marca ma ON v.marca_id = ma.id
INNER JOIN api_telemetria_modelo mo ON v.modelo_id = mo.id
INNER JOIN api_telemetria_medicao med ON mv.medicao_id = med.id
INNER JOIN api_telemetria_unidademedida um ON med.unidade_medida_id = um.id
ORDER BY mv.data DESC;
```

**Objetivo:** Validar todos os relacionamentos do sistema em uma única query.

---

## 4. Medições de um Veículo Específico (WHERE com JOIN)

```sql
SELECT 
    v.descricao AS veiculo,
    ma.nome AS marca,
    mo.nome AS modelo,
    med.tipo AS tipo_medicao,
    um.nome AS unidade_medida,
    mv.valor,
    mv.data
FROM api_telemetria_medicaoveiculo mv
INNER JOIN api_telemetria_veiculo v ON mv.veiculo_id = v.id
INNER JOIN api_telemetria_marca ma ON v.marca_id = ma.id
INNER JOIN api_telemetria_modelo mo ON v.modelo_id = mo.id
INNER JOIN api_telemetria_medicao med ON mv.medicao_id = med.id
INNER JOIN api_telemetria_unidademedida um ON med.unidade_medida_id = um.id
WHERE v.id = 1
ORDER BY mv.data DESC;
```

**Objetivo:** Buscar histórico completo de medições de um veículo específico.

---

## 5. Quantidade de Medições por Veículo (GROUP BY com COUNT)

```sql
SELECT 
    v.id,
    v.descricao AS veiculo,
    ma.nome AS marca,
    mo.nome AS modelo,
    COUNT(mv.id) AS total_medicoes
FROM api_telemetria_veiculo v
INNER JOIN api_telemetria_marca ma ON v.marca_id = ma.id
INNER JOIN api_telemetria_modelo mo ON v.modelo_id = mo.id
LEFT JOIN api_telemetria_medicaoveiculo mv ON v.id = mv.veiculo_id
GROUP BY v.id, v.descricao, ma.nome, mo.nome
ORDER BY total_medicoes DESC;
```

**Objetivo:** Identificar quais veículos têm mais medições registradas.

---

## 6. Última Medição de Cada Veículo (Subquery com MAX)

```sql
SELECT 
    v.descricao AS veiculo,
    ma.nome AS marca,
    med.tipo AS tipo_medicao,
    mv.valor,
    mv.data AS ultima_medicao
FROM api_telemetria_veiculo v
INNER JOIN api_telemetria_marca ma ON v.marca_id = ma.id
INNER JOIN api_telemetria_medicaoveiculo mv ON v.id = mv.veiculo_id
INNER JOIN api_telemetria_medicao med ON mv.medicao_id = med.id
WHERE mv.data = (
    SELECT MAX(mv2.data)
    FROM api_telemetria_medicaoveiculo mv2
    WHERE mv2.veiculo_id = v.id
)
ORDER BY v.id;
```

**Objetivo:** Obter a medição mais recente de cada veículo.

---

## 7. Medições por Período (Filtro de Data)

```sql
SELECT 
    v.descricao AS veiculo,
    ma.nome AS marca,
    med.tipo AS tipo_medicao,
    mv.valor,
    mv.data
FROM api_telemetria_medicaoveiculo mv
INNER JOIN api_telemetria_veiculo v ON mv.veiculo_id = v.id
INNER JOIN api_telemetria_marca ma ON v.marca_id = ma.id
INNER JOIN api_telemetria_medicao med ON mv.medicao_id = med.id
WHERE mv.data BETWEEN '2024-01-01' AND '2024-12-31'
ORDER BY mv.data DESC;
```

**Objetivo:** Filtrar medições por período específico.

---

## 8. Veículos por Marca (GROUP BY)

```sql
SELECT 
    ma.nome AS marca,
    COUNT(v.id) AS total_veiculos
FROM api_telemetria_marca ma
LEFT JOIN api_telemetria_veiculo v ON ma.id = v.marca_id
GROUP BY ma.id, ma.nome
ORDER BY total_veiculos DESC;
```

**Objetivo:** Contar quantos veículos existem por marca.

---

## 9. Verificar Integridade Referencial (CASCADE)

```sql
-- Primeiro, verificar veículos de uma marca específica
SELECT 
    v.id, 
    v.descricao, 
    ma.nome AS marca
FROM api_telemetria_veiculo v
INNER JOIN api_telemetria_marca ma ON v.marca_id = ma.id
WHERE ma.id = 1;

-- Depois executar DELETE para testar CASCADE (CUIDADO: isso remove dados!)
-- DELETE FROM api_telemetria_marca WHERE id = 1;
-- Os veículos relacionados devem ser deletados automaticamente devido ao CASCADE
```

**Objetivo:** Validar que o `on_delete=models.CASCADE` está funcionando corretamente.

---

## 10. Média de Valores por Tipo de Medição (AVG)

```sql
SELECT 
    med.tipo AS tipo_medicao,
    um.nome AS unidade_medida,
    COUNT(mv.id) AS total_registros,
    AVG(mv.valor) AS valor_medio,
    MIN(mv.valor) AS valor_minimo,
    MAX(mv.valor) AS valor_maximo
FROM api_telemetria_medicao med
INNER JOIN api_telemetria_unidademedida um ON med.unidade_medida_id = um.id
LEFT JOIN api_telemetria_medicaoveiculo mv ON med.id = mv.medicao_id
GROUP BY med.id, med.tipo, um.nome
ORDER BY total_registros DESC;
```

**Objetivo:** Análise estatística das medições por tipo.

---

## Como Executar

1. Acesse o MySQL:
   ```bash
   mysql -u root -p
   ```

2. Selecione o banco de dados:
   ```sql
   USE telemetria;
   ```

3. Execute as queries acima para validar os dados.

## Observações

- Todas as queries usam JOINs para validar relacionamentos entre tabelas
- As queries estão ordenadas por complexidade crescente
- Sempre teste queries de DELETE em ambiente de desenvolvimento primeiro
