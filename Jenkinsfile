pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'siriusblack4210/devops-movie'
        GIT_REPO = 'https://github.com/shreyashpatil4266/devops-movie.git'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git credentialsId: 'github-creds', url: "${env.GIT_REPO}"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                        echo $PASS | docker login -u $USER --password-stdin
                        docker push $DOCKER_IMAGE
                    '''
                }
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker stop devops-movie || true
                    docker rm devops-movie || true
                    docker run -d --name devops-movie -p 5000:5000 $DOCKER_IMAGE
                '''
            }
        }

        stage('Push Any Code Changes to GitHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'github-creds', usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PASS')]) {
                    sh '''
                        git config --global user.name "Jenkins"
                        git config --global user.email "jenkins@localhost"
                        git add .
                        git commit -m "Auto commit from Jenkins" || echo "No changes to commit"
                        git push https://$GIT_USER:$GIT_PASS@github.com/shreyashpatil4266/devops-movie.git
                    '''
                }
            }
        }
    }
}
