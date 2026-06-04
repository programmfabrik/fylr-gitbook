# /api/v1/task

Use this endpoint to store & retrieve tasks. A task is a configuration to
run a task module with pre-configured parameters. The tasks are executed in
the background. Tasks can be scheduled to run periodically.

Tasks are user specific. Like exports, tasks are run under as the user who created the task. When listing tasks, only the creating user can see his tasks.

Every task operation requires the system right `system.task` (a
`system.root` user is also accepted). An unauthenticated request returns
`401` with code `UserRequired`; an authenticated user lacking `system.task`
(and not `system.root`) returns `403` with code `SystemRightRequired`.
The id-addressed operations `GET /task/{taskId}/log`,
`POST /task/{taskId}/cancel` and `DELETE /task/{taskId}` load the task by
id and then reject a caller who is neither the task's owner nor a
`system.root` user with `403` code `InsufficientRights`. The list and
`GET /task/{taskId}` instead filter by the session user, so another
user's tasks are simply not returned (an unknown id yields `404`).

### `GET /task`
{% swagger src="./fylr-openapi.yml" path="/task" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `POST /task`
{% swagger src="./fylr-openapi.yml" path="/task" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `PUT /task`
{% swagger src="./fylr-openapi.yml" path="/task" method="put" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /task/{taskId}/log`
{% swagger src="./fylr-openapi.yml" path="/task/{taskId}/log" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `POST /task/{taskId}/cancel`
{% swagger src="./fylr-openapi.yml" path="/task/{taskId}/cancel" method="post" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /task/{taskId}`
{% swagger src="./fylr-openapi.yml" path="/task/{taskId}" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `PATCH /task/{taskId}`
{% swagger src="./fylr-openapi.yml" path="/task/{taskId}" method="patch" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `DELETE /task/{taskId}`
{% swagger src="./fylr-openapi.yml" path="/task/{taskId}" method="delete" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}

### `GET /task/modules`
{% swagger src="./fylr-openapi.yml" path="/task/modules" method="get" %}
[fylr-openapi.yml](./fylr-openapi.yml)
{% endswagger %}
