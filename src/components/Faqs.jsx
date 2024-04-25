import Image from 'next/image'

import { Container } from '@/components/Container'
import backgroundImage from '@/images/background-faqs.jpg'

const faqs = [
  [
    {
      question: 'Why does this even exist?',
      answer:
        'We are not sure, but we are pretty sure it’s not for any good reason.',
    },
    {
      question: 'Can I pay with Bitcoin?',
      answer:
        'Sure, just send us an email appletune@kernelguardian.com and we will send you our wallet address.',
    },
    {
      // Funny question and answer
      question: 'Is this a joke?',
      answer: 'No, but we are working on it.',
    },
  ],
  [
    {
      question: 'What is the best way to get in touch with support?',
      answer: 'support@kernelguardian.com',
    },
    {
      question: 'Do you have a mobile app? I can’t find it in the app store.',
      answer:
        'No, we don’t have a mobile app. We are still trying to figure out how to make a website. 😶‍🌫️',
    },
    {
      question: 'Is this a real company? Are you incorporated?',
      answer: 'Honestly, IDK. ',
    },
  ],
  [
    {
      question: 'Can I hire you to create something for me?',
      answer:
        'Sure, send us an email with your requirements and we will get back to you with a quote. We are not cheap. 💸',
    },
    {
      question: 'Can we expect more features?',
      answer: 'In life it’s really better to never expect anything at all. 🤷‍♂️',
    },
    {
      question: 'Who are you even? What is your name?',
      answer:
        'You can find more about me by visiting my website: kernelguardian.com. 🤓',
    },
  ],
]

export function Faqs() {
  return (
    <section
      id="faq"
      aria-labelledby="faq-title"
      className="relative overflow-hidden bg-slate-50 py-20 sm:py-32"
    >
      <Image
        className="absolute left-1/2 top-0 max-w-none -translate-y-1/4 translate-x-[-30%]"
        src={backgroundImage}
        alt=""
        width={1558}
        height={946}
        unoptimized
      />
      <Container className="relative">
        <div className="mx-auto max-w-2xl lg:mx-0">
          <h2
            id="faq-title"
            className="font-display text-3xl tracking-tight text-slate-900 sm:text-4xl"
          >
            Frequently asked questions
          </h2>
          <p className="mt-4 text-lg tracking-tight text-slate-700">
            If you can’t find what you’re looking for, email our support team
            and if you’re lucky someone will get back to you.
          </p>
        </div>
        <ul
          role="list"
          className="mx-auto mt-16 grid max-w-2xl grid-cols-1 gap-8 lg:max-w-none lg:grid-cols-3"
        >
          {faqs.map((column, columnIndex) => (
            <li key={columnIndex}>
              <ul role="list" className="flex flex-col gap-y-8">
                {column.map((faq, faqIndex) => (
                  <li key={faqIndex}>
                    <h3 className="font-display text-lg leading-7 text-slate-900">
                      {faq.question}
                    </h3>
                    <p className="mt-4 text-sm text-slate-700">{faq.answer}</p>
                  </li>
                ))}
              </ul>
            </li>
          ))}
        </ul>
      </Container>
    </section>
  )
}
