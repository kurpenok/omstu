#include <iostream>
#include <limits.h>
#include <string.h>
#include <queue>

#define V 6

int bfs(int rGraph[V][V], int s, int t, int parent[]) {
    bool visited[V];
    memset(visited, 0, sizeof(visited));

    std::queue<int> q;
    q.push(s);
    visited[s] = true;
    parent[s] = -1;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v = 0; v < V; v++) {
            if (visited[v]==false && rGraph[u][v] > 0) {
                q.push(v);
                parent[v] = u;
                visited[v] = true;
            }
        }
    }

    return (visited[t] == true);
}

void dfs(int rGraph[V][V], int s, bool visited[]) {
    visited[s] = true;
    for (int i = 0; i < V; i++)
       if (rGraph[s][i] && !visited[i])
           dfs(rGraph, i, visited);
}

void minCut(int graph[V][V], int s, int t) {
    int rGraph[V][V];
    
    int v, u;

    for (u = 0; u < V; u++)
        for (v = 0; v < V; v++)
             rGraph[u][v] = graph[u][v];

    int parent[V];

    int max_flow = 0;
    while (bfs(rGraph, s, t, parent)) {
        int path_flow = INT_MAX;
        for (v = t; v != s; v = parent[v]) {
            u = parent[v];
            path_flow = std::min(path_flow, rGraph[u][v]);
        }

        for (v = t; v != s; v = parent[v]) {
            u = parent[v];
            rGraph[u][v] -= path_flow;
            rGraph[v][u] += path_flow;
        }

        std::cout << "[+] Pathflow: " << path_flow << std::endl;
        max_flow += path_flow;
    }

    bool visited[V];
    memset(visited, false, sizeof(visited));
    dfs(rGraph, s, visited);

    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            if (visited[i] && !visited[j] && graph[i][j]) {
                std::cout << i << " - " << j << std::endl;
                std::cout << graph[i][j] << std::endl;
            }
        }
    }
    std::cout << "[+] Maximum flow total: " << max_flow << std::endl;

    return;
}

int main() {
    int graph[V][V] = {
        {0, 53, 87, 0, 15, 0},
        {0, 0, 13, 22, 44, 72},
        {0, 0, 0, 17, 31, 14},
        {0, 0, 0, 0, 16, 0},
        {0, 0, 0, 7, 0, 84},
        {0, 0, 0, 0, 0, 0}
    };

    minCut(graph, 0, 5);

    return 0;
}

