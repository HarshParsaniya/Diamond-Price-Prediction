@Library('Shared') _
pipeline{
    
    agent { label "kk" }
    
    stages{
        stage("Hello"){
            steps{
                script{
                    hello()
                }
            }
        }
        stage("Code"){
            steps{
                echo "Code cloning is start..."
                script{
                    clone('https://github.com/HarshParsaniya/Diamond-Price-Prediction.git', 'main')
                }
                echo "Code cloning successful"
            }
        }
        stage("Build"){
            steps{
                echo "Code building is start..."
                script{
                    docker_build("diamond-webapp", "latest", 'harshpatel4877')
                }
                echo "Code building successful"
            }
        }
        stage("Push"){
            when {
                expression { return params.PUSH_IMAGE == true }
            }
            steps{
                echo "Code pushing in dockerhub is start..."
                docker_push("diamond-webapp", "latest", "harshpatel4877")
                echo "Code pusing in dockerhub successful"
            }
        }
        stage("Test"){
            steps{
                echo "Code testing is start..."
                echo "Code testing successful"
            }
        }
        stage("Deploy"){
            steps{
                echo "Code deploying is start..."
                sh "docker compose down && docker compose up -d"
                echo "Code deploying successful"
            }
        }
    }
}
