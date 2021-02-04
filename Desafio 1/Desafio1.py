import pm4py
from pm4py.objects.log.log import EventLog

from pm4py.algo.filtering.log.attributes import attributes_filter
from pm4py.algo.filtering.log.end_activities import end_activities_filter
from pm4py.algo.filtering.log.start_activities import start_activities_filter
from pm4py.objects.log.importer.xes import importer as xes_importer
log = xes_importer.apply("running-example.xes")

print("__________________________")

print(sum([len(trace) for trace in log])) # Soma a quantidade de eventos de cada trace

print("__________________________")

print("Atividades do processo:")
activities = attributes_filter.get_attribute_values(log, "concept:name")
print(activities) # Mostra cada atividade com o numero de vezes que ela apareceu ao lado
print("__________________________")

print("Recursos do processo:")
resources = attributes_filter.get_attribute_values(log, "org:resource")
print("__________________________")

print("Atividade inicial")
log_sa = start_activities_filter.get_start_activities(log) # Filtra a atividade inicial
print(log_sa)

print("__________________________")

print("Atividade Final")
log_ea = end_activities_filter.get_end_activities(log) # Filtra a atividade final
print(log_ea)

print("__________________________")

print("Traces com duração acima de 5 dias:")
from pm4py.algo.filtering.log.cases import case_filter
five_days = case_filter.filter_case_performance(log, 432000, 86400000) # filtra os traces com tempo de duração maior que 5 dias
print(five_days)

#__________________________
#filtragem de variantes
from pm4py.algo.filtering.log.variants import variants_filter
variants = variants_filter.get_variants(log) # obtem as variantes do log
auto_filter_variant = variants_filter.apply_auto_filter(log) # filtro que mantem automaticamente as variantes mais comuns do log
#__________________________
print("__________________________")

# Faça uma filtragem para obter no máximo 10 instâncias (cases) do evento de log
print("Maximo de 10 cases do log")
case_filter = EventLog(log[:min(len(log), 10)])
print(case_filter)

print("__________________________")
# Calcule a média de tempo de execução dos cases analisados no log
from pm4py.statistics.traces.log import case_statistics
median_case_duration = case_statistics.get_median_caseduration(log, parameters={case_statistics.Parameters.TIMESTAMP_KEY: "time:timestamp"})
print(median_case_duration)

print("__________________________")


# Exportando arquivo XES
from pm4py.objects.log.exporter.xes import exporter as xes_exporter
xes_exporter.apply(log, 'D:/logexemplo.xes')
print("__________________________")
