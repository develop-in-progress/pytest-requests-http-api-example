pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "Building with ${params.test_value} parameter"
            }
        }
        stage('Test') {
            steps {
                sh 'python3 --version'
                sh 'pip3 install -r requirements.txt'
                sh 'python3 -m pytest --alluredir=allure-results'
            }
        }
        stage('Reports') {
            steps {
            script {
            allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                    ])
                }
                }
            }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
        post{
        always{
            mail to: "amberlol11x@gmail.com",
        }
    }
    }
}
