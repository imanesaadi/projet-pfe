pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = 'imanesaadi'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Récupération du code depuis GitHub...'
                checkout scm
            }
        }

        stage('Build Images') {
            steps {
                echo 'Construction des images Docker...'
                sh 'docker build -t $DOCKER_HUB_USER/user-service:latest ./services/user-service'
                sh 'docker build -t $DOCKER_HUB_USER/product-service:latest ./services/product-service'
                sh 'docker build -t $DOCKER_HUB_USER/order-service:latest ./services/order-service'
            }
        }

        stage('Test') {
            steps {
                echo 'Lancement des tests...'
                sh 'docker run --rm $DOCKER_HUB_USER/user-service:latest python -c "import flask; print(flask.__version__)"'
                sh 'docker run --rm $DOCKER_HUB_USER/product-service:latest python -c "import flask; print(flask.__version__)"'
                sh 'docker run --rm $DOCKER_HUB_USER/order-service:latest python -c "import flask; print(flask.__version__)"'
            }
        }

        stage('Push Images') {
            steps {
                echo 'Publication des images sur Docker Hub...'
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push $DOCKER_HUB_USER/user-service:latest'
                    sh 'docker push $DOCKER_HUB_USER/product-service:latest'
                    sh 'docker push $DOCKER_HUB_USER/order-service:latest'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline réussi ! Toutes les images sont publiées.'
        }
        failure {
            echo 'Pipeline échoué ! Vérifiez les logs.'
        }
    }
}
