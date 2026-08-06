{{- define "desktop-app-repo.name" -}}
{{- .Chart.Name -}}
{{- end -}}

{{- define "desktop-app-repo.labels" -}}
app: {{ include "desktop-app-repo.name" . }}
{{- end -}}
