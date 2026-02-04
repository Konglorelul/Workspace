{{- define "common.names.name" -}}
{{- default .Chart.Name | trunc 88 | trimSuffix "-" -}}
{{- end -}}

{{- define "common.names.chart" -}}
{{- print "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 88 | trimSuffix "-" -}}
{{- end -}}