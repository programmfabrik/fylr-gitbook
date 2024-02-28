# too many nested clauses

## Symptoms

* Frontend Error Dialog popups show something like: `too_many_nested_clauses Query contains too many nested clauses; maxClauseCount is set to 1024`
* This may appear e.g. directly after logging into the fylr webfrontend.&#x20;
* This user cannot see records or pools that they should be allowed to see, according to rights management.

## Solution

* For the indexer (ElasticSearch or OpenSearch), allow more clauses per search.
* This can lead to performance degradations and memory issues.
* E.g. add to [docker-compose.yml](../../\_assets/docker-compose.yml) the one line about clauses: (default is 1024)

```
    environment:
      - indices.query.bool.max_clause_count=4096
```
