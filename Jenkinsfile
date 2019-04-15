pipeline {
    agent {
        docker { image 'python:3.6' }
    }

    stages {
        stage('Test') {
            steps {
                dir('first-example') {
                    sh 'pip install --user pipenv'
                    sh 'pip run pytest'
                }

                dir('second-example-with-types') {
                    sh 'pip install --user pipenv'
                    sh 'pip run pytest'
                }

                dir('mock-example') {
                    sh 'pip install --user pipenv'
                    sh 'pip run pytest'
                }
            }
        }
    }
}
