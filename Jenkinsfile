pipeline {
  agent any
  stages {
    stage('checkversion') {
      steps {
          sh 'python3 --version'
      }
    }
     stage('run python') {
      steps {
       
        sh 'python3 test.py'
      }
    }

  }
}
