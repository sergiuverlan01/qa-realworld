pipeline {
    agent any

    parameters {
        choice(
            name: 'CAMPAIGN',
            choices: ['smoke', 'regression'],
            description: 'tests campaign which will be run'
        )
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    pip3 install poetry
                    poetry install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh "poetry run pytest -m ${params.CAMPAIGN} -v"
            }
        }
    }

    post {
        always {
            echo "Pipeline finalized. Campanign: ${params.CAMPAIGN}"
        }
        success {
            echo "✅ All tests succeeded!"
        }
        failure {
            echo "❌ Some tests failed!"
        }
    }
}